from os import path
import click

from . import global_config
from .global_config import init_config_dir

from .actions import do_install_app, do_uninstall_app, do_find_app, do_list_app, do_run_config, do_list_config, \
    do_show_config, do_add_config, do_remove_config, do_edit_config, do_rename_config


@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option()
@click.option('--config-directory', type=click.Path(),
              default=global_config.config_dir,
              help='Path to configuration directory')
def projector(ctx, config_directory):
    """
    This script helps to install, manage, and run JetBrains IDEs with Projector.
    """

    global_config.config_dir = config_directory

    if not path.isdir(global_config.config_dir):  # first time run with this config
        init_config_dir()
        print("Please select IDE to install:")
        do_install_app(None)
        do_run_config(None)

    elif not ctx.invoked_subcommand:
        click.echo(ctx.get_help())


@projector.group()
def ide():
    """
    JetBrains IDEs management commands
    """
    pass


@ide.command(short_help='Find Projector-compatible IDE')
@click.argument('pattern', type=click.STRING, required=False)
def find(pattern):
    """projector ide find [pattern]

    Find projector-compatible IDE with the name matching to the given pattern.
    If no pattern is specified, finds all the compatible IDEs.
    """
    do_find_app(pattern)


@click.command(short_help='Install and configure selected IDE')
@click.argument('ide_name', type=click.STRING, required=False)
def install_app(ide_name):
    """projector ide install [ide_name]

    Parameter ide_name is the name of IDE to install.
    If no IDE name is given or the pattern is ambiguous, guides the user through the install process.
    """
    do_install_app(ide_name)


ide.add_command(install_app, name='install')


@ide.command(short_help='Uninstall selected IDE')
@click.argument('name_pattern', type=click.STRING, required=False)
def uninstall(name_pattern):
    """projector ide install [ide_name_pattern]

    Parameter ide_name_pattern is matched to the name of IDE to uninstall.
    If no name pattern is given or the pattern is ambiguous, guides the user through the uninstall process.
    """
    do_uninstall_app(name_pattern)


@click.command(short_help='Display installed IDEs')
@click.argument('pattern', type=click.STRING, required=False)
def list_apps(pattern):
    """projector ide list [pattern]

    Displays installed IDEs whose names matches to given pattern.
    If no pattern is given, lists all installed IDEs.
    """
    do_list_app(pattern)


ide.add_command(list_apps, name='list')


@projector.group()
def config():
    """
    Configuration management commands
    """
    pass


@click.command(short_help='Run selected config')
@click.argument('config_name', type=click.STRING, required=False)
def run_config(config_name):
    """projector config run config_name_pattern

    Parameter config_name_pattern specifies the configuration to run.
    If no configuration specified or the pattern is ambiguous, selects a configuration interactively.
    """
    do_run_config(config_name)


config.add_command(run_config, name='run')


@click.command(short_help='List configurations')
@click.argument('pattern', required=False)
def list_config(pattern):
    """projector config list [pattern]

    Displays configurations whose names matches to the given pattern.
    If no pattern is given, lists all the configurations.
    """
    do_list_config(pattern)


config.add_command(list_config, name='list')


@config.command(short_help='Show selected configuration details')
@click.argument('config_name', type=click.STRING, required=False)
def show(config_name):
    """projector config show [config_name]

    Parameter config_name specifies a desired configuration.
    If not given or ambiguous, selects a configuration interactively.
    """
    do_show_config(config_name)


@config.command(short_help='Add new configuration')
@click.argument('config_name', type=click.STRING, required=False)
@click.argument('ide_path', type=click.STRING, required=False)
def add(config_name, ide_path):
    """projector config add [config_name]

    Add a new configuration.
    """
    do_add_config(config_name, ide_path)


@config.command(short_help='Remove configuration')
@click.argument('config_name', type=click.STRING, required=False)
def remove(config_name):
    """projector config remove [config_name]

    Remove an existing configuration.
    """
    do_remove_config(config_name)


@config.command(short_help='Change existing configuration')
@click.argument('config_name', type=click.STRING, required=False)
def edit(config_name):
    """projector config edit [config_name]

    Change an existing configuration.
    """
    do_edit_config(config_name)


@config.command(short_help='Rename existing configuration')
@click.argument('from_name', type=click.STRING, required=True)
@click.argument('to_name', type=click.STRING, required=True)
def rename(from_name, to_name):
    """projector config rename from_config_name to_config_name

    Rename an existing configuration.
    """
    do_rename_config(from_name, to_name)


# Projector commands shortcuts

@projector.command(short_help='Run selected configuration')
@click.argument('config_name', type=click.STRING, required=False)
def run(config_name):
    """projector run config_name

    Shortcut for projector config run config_name
    """
    do_run_config(config_name)


@projector.command(short_help='Install and configure selected IDE')
@click.argument('ide_name', type=click.STRING, required=False)
def install(ide_name):
    """projector install [ide_name]

    Shortcut for projector ide install [ide_name]
    """
    do_install_app(ide_name)


@projector.command(short_help='Find available IDEs')
@click.argument('pattern', type=click.STRING, required=False)
def find(pattern):
    """projector find [pattern]

    Shortcut for projector ide find [pattern]
    """
    do_find_app(pattern)