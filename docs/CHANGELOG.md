# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.7.2] - 2023-01-12

- Removed all underscore characters in CHANGELOG.md to (hopefully) fix formatting issues

## [2.7.1] - 2023-01-12

### Fixed

- Added missing commands to the !help() commands list

## [2.7.0] - 2023-01-12

### Changed

- Split configure.py into two modules: configure.py and readconfigs.py
- All config.ini reads are now done within readconfigs.py
- All configuration entries are now treated as constants in the modules which use them

### Added

- DELETIONTIME configuration setting for auto-delete messages

### Removed

- Removed **many** now-deprecated imports from config.ini in harbinger.py

### Fixed

- Formatted all modules
- Sorted imports in all modules

## [2.6.1] - 2023-30-11

### Added

- !help() command messages for all cogs.dev commands

### Fixed

- Previously-uncaught exception in !changelog() when MissingRole
- !changelog() output no longer auto-deletes

## [2.6.0] - 2023-30-11

### Added

- Dev Cog: allows for arbitrary cogs to be loaded/unloaded without shutting down the bot
- config.ini: deletion-timer to determine when to autodelete system messages from the channel (errors, etc.)
- Various error messages

### Fixed

- Minor formatting
- Command messages printing improperly/at the wrong time

### Changed

- Behavior of cog loading in harbinger.py: cogs now are loaded through a list rather than individually

### Known Issues

- Missing !help() commands for all dev commands
- Missing error message for !changelog() when missing required role
- Output of !changelog() should not autodelete

## [2.5.0] - 2023-30-11

### Added

- Role checks: moderation commands now require moderator role
- Role checks: status commands now require developer role

### Fixed

- Configure.py now writes Role IDs to config.ini
- Minor formatting throughout

## [2.4.1] - 2023-30-11

### Fixed

- Removed redundant !bug() command in status cog which was causing problems with sending the entire message

## [2.4.0] - 2023-29-11

### Removed

- cogs/help.py

### Added

- cogs/helprewrite.py (name will be changed next version)

## [2.3.1] - 2023-29-11

### Fixed

- !lmgtfy now accepts an abritrary number of arguments (without quotes)
- !add now adds an arbitrary number of values
- !say now accepts an arbitrarily long message (no longer requires quoting)
- !ask now accepts an arbitrary-length message (no need to quote)

### Added

- !ask command, to act similarly to a Magic 8ball

### Removed

- Unused imports

## [2.3.0] - 2023-29-11

### Deprecated

- !joined() command

### Added

- !whois() function to get detailed member information
- Help message(s) for new function(s)

### Fixed

- Minor formatting

## [2.2.2] - 2023-29-11

### Removed

- Unused function calls in moderation cog

### Added

- serverinfo command to view server details and member list

### Fixed

- Formatting throughout

## [2.2.1] - 2023-29-11

### Added

- Help messages for all music commands
- Various music playback commands (join, leave, stream, play, pause)

### Fixed

- Some help embeds not sending as expected

### Deprecated

- yt() commmand has been replaced with stream() command to avoid confusion regarding which URLs may be played

## [2.2.0] - 2023-28-11

### Added

- Music playing functionality (thus far, only !join and !yt commands implemented)

### Fixed

- Formatting throughout

## [2.1.1] - 2023-28-11

### Added

- !bug command to email bug reports to owner/developer

## [2.1.0] - 2023-28-11

### Changed

- User configuration information no longer saved in plaintext: now encodes all config.ini entries to base64 for security reasons

## [2.0.2] - 2023-25-11

### Fixed

- Minor formatting throughout
- Removed unused imports and functions

## [2.0.1] - 2023-25-11

### Fixed

- Custom color should now import correctly from config file

### Changed

- Name of custom color within config.ini

## [2.0.0] - 2023-25-11

### MAJOR UPDATE

- Nearly *complete* overhaul of module
- **ALL** bot commands should now be fully supported

### Added

- !switch command(s)
- !mccmd command
- /docs/examples/ dir to house default config files
- /config/ dir to house user config file(s)

### Fixed

- Config files now load correctly throughout entire module
- Color designation should now work throughout module
- Ran Black formatter throughout

### Removed

- utils/server-agent.py
- many unused imports throughtout

### Changed

- !mccmd and !switch commands no longer use SSH
- Startup now managed by start.sh
- Location of config file(s): /docs/examples/config.ini, /docs/examples/start.conf
- Config file(s) now have a dedicated location

## [1.6.4] - 2023-18-11

### Added

- Substantial information to README.md

### Formatting

- Ran Black formatter throughout module

## [1.6.3] - 2023-18-11

### Fixed

- tmux now behaves correctly within start.sh
- !help command now returns help information for Minecraft server side commands

### Changed

- start.sh now launches both the bot and the MC server

## [1.6.2] - 2023-18-11

### Fixed

- ConfigParser should work now

### Added

- Started to add code for upcoming start script(s)

### Changed

- Script should launch from start script going forward

## [1.6.1] - 2023-18-11

### Added

- docs/sample-env file for end-user configuration

### Removed

- errant **pycache** files that may have been included in the repo

## [1.6.0] - 2023-18-11

### Fixed

- lmgtfy function
- define function
- ping function
- repo was all jacked up from poor commits

### Changed

- namespace for Helpers.timestamp (now harbinger.timestamp)

## [1.5.0] - 2023-10-11

### Major Update

- Refactored almost every function in package
- Consolidated many needlessly-verbose and complex functions into much more easily-understood alternatives

## Deprecated

- main.py has been removed and its functionality merge into harbinger.py

## Added

- harbinger.py takes the place of main.py as the entry point for the system
- New cog: mc-server

## [1.4.0] - 2023-10-11

### Changed

- Refactored many functions throughout Cogs
- Cleaned up redundant functions calls and unused imports throughout codebase

### Bugfixes

- Attempting to (further) improve imports

### Added

- **init.py** to utils

### Changed

- ServerAgent is now its own class (I'm not 100% this helps at all, but I'm learning)

## [1.3.3] 2023-09-11

### Changed

- Wrote README.md (still need more information about configuring everything)
- Incremented version.

## [1.3.2] - 2023-09-11

### Bugfixes

- Imports should all work correctly now
- Error handling introduced in some areas
- All cogs load correctly

### Changed

- Rewrote .env file to make config easier
- Renamed some variables, constants, and functions to unobfuscate their function

## [1.3.1] - 2023-09-11

### MAJOR RELEASE VERSION

### Added

- !commandMc command to send console commands to the Minecraft server
- !switch <on|off> to start and stop the Minecraft server

### Changed

- Majorly reworked the way some imports interact
- Added some new dependancies
- Updated requirements.txt

## [1.3.0] - 2023-09-11

### Major Update

- !harbinger command now functions (somewhat, usually).  lots and lots to do now, can't list it all right here! Check [GitHub](https://github.com/notoriouslogank/harbinger/issues).

## [1.2.1] - 2023-08-11

### Fixed

- Cog loading messages now appear in correct order

### Added

- Missing docstring(s) in !help command

## [1.2.0] - 2023-08-11

### Breaking Changes

- Restructured entire module: created harbinger/utils/, harbinger/server.utils, harbinger/docs folders to contain source code
- Changed most instances of importing helpers.py: imports are much more streamlined

### Added

- !define command to get the Meriam-Webster definition of a word
- !help command description: !define

### Fixed

- Minor formatting errors in CHANGELOG.md
- !changelog command

## [1.1.6] - 2023-08-11

### Changed

-Reformatted the embed created by !help

## [1.1.5] - 2023-08-11

### Fixed

- Formatting errors in README.md
- Removed unused import in help.py

### Added

- Link to GitHub Issue Tracker in !help embed

### Changed

- Rewrote all docstrings for brevity and clarity.
- Removed two (ostensibly) unused imports in helpers.py
- Rewrote all !help command descriptions

### Removed

- Unused mc.sh file

## [1.1.4] - 2023-08-11

### Deprecated

- getLog() helper function; obsoleted by !changelog()

### Added

- on ready messages for each Cog
- embed for !changelog command

### Changed

- !changelog command now sends embed

### Fixed

- !changelog command works properly now
- Minor formatting errors in CHANGELOG.md

## [1.1.3] - 2023-07-11

### Added

- Custom MyHelpCommand to replace defaulHelpCommand
- Custom help message for every user engagable bot command
- Avatar to help message; will be deploying this further in future updates

### Removed

- Default !help function

## [1.1.2] - 2023-07-11

### Changed

- Default !help() command no longer uses automatic arguments and instead defaults to docstring args

### Added

- Descriptions for arguments in !help() function

## [1.1.1] - 2023-07-11

### Changed

- BotStatus cog renamed to Status

### Added

-Docstrings for all commands (cogs/)

### Fixed

- All cogs should work as intended now
- Imports should work correctly throughout
- Reformatted entire codebase (Black formatter)
- Sorted imports correctly (isort)

### Removed

- Unused imports throughout module

## [1.0.3-dev] - 2023-07-11

### Added

- cogs/ directory for transition to cog-based commands
- cogs/moderation.py: moderation commands
- cogs/status.py: bot status and info commands
- cogs/tools.py: useful commands, tools, etc. the bot can access

## [1.0.2] - 2023-07-11

## Removed

- All logging support; will be migrating to proprietary log format because logging sucks in this module

### Changed

- !lmgtfy() now returns a separate message with only the query string
- log file name changed to 'harbinger.log'

### Fixed

- Minor formatting errors in CHANGELOG.md

## [1.0.1] - 2023-07-11

### Added

- !playing() command to post game information
- sample-env
- lmgtfy() *may* now send the requesting user a DM with their query string

## [0.9.9] - 2023-06-11

### Fixed

- Minor formatting problems with CHANGELOG.md

### Changed

- Certain commands now auto-remove the original command to obfuscate the sender

## [0.9.8] - 2023-06-11

### Fixed

- Minor formatting issues

### Removed

- Unused functions

## [0.9.7] - 2023-06-11

### Changed

- Sorted imports with isort

## [0.9.6] - 2023-06-11

### Fixed

- Clear command now functions as expected

### Changed

- Moved Channel ID to .env as CHANNEL

### Removed

- Unused imports

## [0.9.5] - 2023-06-11

### Added

- Delete command to have the bot silently delete messages.
- onmessage check for 'curse' words

## [0.9.4] - 2023-06-11

### Changed

- Names of several minor functions (helpers.timestamp() is now imported simply as timestamp(), for example.)
- Sequencing of some functions, mostly as a matter of formatting

### Fixed

- Minor formatting errors

### Added

- Docstrings to all bot commands
- helpers.py module to contain non-bot commands and events

### Removed

- Unused imports

## [0.9.1] - 2023-04-11

### Added

- say() command
- getLog()
- console messages about current status

### Fixed

- changelog() *should* work now

### Deprecated

- getChangelog()

## [0.9.0]

### Added

- getChangelog()
- !changelog command

## [0.8.5] - 2023-04-11

### Deprecated

- Command online() replaced with status()

### Changed

- Formatted main.py using Black formatter

### Bugfixes

- Removed all log messages containing variables (may not be callable?)

## [0.8.4] - 2023-04-11

### Changed

- Temporarily disable automatic versioning due to possible bug(s)

### Bugfixes

- Removed most log messages to attempt to alleviate error(s)

## [0.8.3] - 2023-04-11

### Added

- .vscode settings directory to .gitignore

## [0.8.2] - 2023-04-11

### Added

- Logging support for many (all?) commands

## [0.8.1] - 2023-04-11

### Fixed

- Semantic version now increments automatically (from this file)

### Added

- getVer() function to source the semantic version info from CHANGELOG.md

## [0.8.0] - 2023-04-11

### Added

- requirements.txt
- Content to README.md

### Changed

- Edited CHANGELOG.md for formatting

## [0.7.7] - 2023-04-11

### Added

- CHANGELOG.md

### Changed

- Updated .gitignore
=======

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.2] - 2023-25-11

### Fixed

- Minor formatting throughout
- Removed unused imports and functions

## [2.0.1] - 2023-25-11

### Fixed

- Custom color should now import correctly from config file

### Changed

- Name of custom color within config.ini

## [2.0.0] - 2023-25-11

### MAJOR UPDATE

- Nearly *complete* overhaul of module
- **ALL** bot commands should now be fully supported

### Added

- !switch command(s)
- !mccmd command
- /docs/examples/ dir to house default config files
- /config/ dir to house user config file(s)

### Fixed

- Config files now load correctly throughout entire module
- Color designation should now work throughout module
- Ran Black formatter throughout

### Removed

- utils/server-agent.py
- many unused imports throughtout

### Changed

- !mccmd and !switch commands no longer use SSH
- Startup now managed by start.sh
- Location of config file(s): /docs/examples/config.ini, /docs/examples/start.conf
- Config file(s) now have a dedicated location

## [1.6.4] - 2023-18-11

### Added

- Substantial information to README.md

### Formatting

- Ran Black formatter throughout module

## [1.6.3] - 2023-18-11

### Fixed

- tmux now behaves correctly within start.sh
- !help command now returns help information for Minecraft server side commands

### Changed

- start.sh now launches both the bot and the MC server

## [1.6.2] - 2023-18-11

### Fixed

- ConfigParser should work now

### Added

- Started to add code for upcoming start script(s)

### Changed

- Script should launch from start script going forward

## [1.6.1] - 2023-18-11

### Added

- docs/sample-env file for end-user configuration

### Removed

- errant **pycache** files that may have been included in the repo

## [1.6.0] - 2023-18-11

### Fixed

- lmgtfy function
- define function
- ping function
- repo was all jacked up from poor commits

### Changed

- namespace for Helpers.timestamp (now harbinger.timestamp)

## [1.5.0] - 2023-10-11

### Major Update

- Refactored almost every function in package
- Consolidated many needlessly-verbose and complex functions into much more easily-understood alternatives

## Deprecated

- main.py has been removed and its functionality merge into harbinger.py

## Added

- harbinger.py takes the place of main.py as the entry point for the system
- New cog: mc-server

## [1.4.0] - 2023-10-11

### Changed

- Refactored many functions throughout Cogs
- Cleaned up redundant functions calls and unused imports throughout codebase

### Bugfixes

- Attempting to (further) improve imports

### Added

- **init.py** to utils

### Changed

- ServerAgent is now its own class (I'm not 100% this helps at all, but I'm learning)

## [1.3.3] 2023-09-11

### Changed

- Wrote README.md (still need more information about configuring everything)
- Incremented version.

## [1.3.2] - 2023-09-11

### Bugfixes

- Imports should all work correctly now
- Error handling introduced in some areas
- All cogs load correctly

### Changed

- Rewrote .env file to make config easier
- Renamed some variables, constants, and functions to unobfuscate their function

## [1.3.1] - 2023-09-11

### MAJOR RELEASE VERSION

### Added

- !commandMc command to send console commands to the Minecraft server
- !switch <on|off> to start and stop the Minecraft server

### Changed

- Majorly reworked the way some imports interact
- Added some new dependancies
- Updated requirements.txt

## [1.3.0] - 2023-09-11

### Major Update

- !harbinger command now functions (somewhat, usually).  lots and lots to do now, can't list it all right here! Check [GitHub](https://github.com/notoriouslogank/harbinger/issues).

## [1.2.1] - 2023-08-11

### Fixed

- Cog loading messages now appear in correct order

### Added

- Missing docstring(s) in !help command

## [1.2.0] - 2023-08-11

### Breaking Changes

- Restructured entire module: created harbinger/utils/, harbinger/server.utils, harbinger/docs folders to contain source code
- Changed most instances of importing helpers.py: imports are much more streamlined

### Added

- !define command to get the Meriam-Webster definition of a word
- !help command description: !define

### Fixed

- Minor formatting errors in CHANGELOG.md
- !changelog command

## [1.1.6] - 2023-08-11

### Changed

-Reformatted the embed created by !help

## [1.1.5] - 2023-08-11

### Fixed

- Formatting errors in README.md
- Removed unused import in help.py

### Added

- Link to GitHub Issue Tracker in !help embed

### Changed

- Rewrote all docstrings for brevity and clarity.
- Removed two (ostensibly) unused imports in helpers.py
- Rewrote all !help command descriptions

### Removed

- Unused mc.sh file

## [1.1.4] - 2023-08-11

### Deprecated

- getLog() helper function; obsoleted by !changelog()

### Added

- on ready messages for each Cog
- embed for !changelog command

### Changed

- !changelog command now sends embed

### Fixed

- !changelog command works properly now
- Minor formatting errors in CHANGELOG.md

## [1.1.3] - 2023-07-11

### Added

- Custom MyHelpCommand to replace defaulHelpCommand
- Custom help message for every user engagable bot command
- Avatar to help message; will be deploying this further in future updates

### Removed

- Default !help function

## [1.1.2] - 2023-07-11

### Changed

- Default !help() command no longer uses automatic arguments and instead defaults to docstring args

### Added

- Descriptions for arguments in !help() function

## [1.1.1] - 2023-07-11

### Changed

- BotStatus cog renamed to Status

### Added

-Docstrings for all commands (cogs/)

### Fixed

- All cogs should work as intended now
- Imports should work correctly throughout
- Reformatted entire codebase (Black formatter)
- Sorted imports correctly (isort)

### Removed

- Unused imports throughout module

## [1.0.3-dev] - 2023-07-11

### Added

- cogs/ directory for transition to cog-based commands
- cogs/moderation.py: moderation commands
- cogs/status.py: bot status and info commands
- cogs/tools.py: useful commands, tools, etc. the bot can access

## [1.0.2] - 2023-07-11

## Removed

- All logging support; will be migrating to proprietary log format because logging sucks in this module

### Changed

- !lmgtfy() now returns a separate message with only the query string
- log file name changed to 'harbinger.log'

### Fixed

- Minor formatting errors in CHANGELOG.md

## [1.0.1] - 2023-07-11

### Added

- !playing() command to post game information
- sample-env
- lmgtfy() *may* now send the requesting user a DM with their query string

## [0.9.9] - 2023-06-11

### Fixed

- Minor formatting problems with CHANGELOG.md

### Changed

- Certain commands now auto-remove the original command to obfuscate the sender

## [0.9.8] - 2023-06-11

### Fixed

- Minor formatting issues

### Removed

- Unused functions

## [0.9.7] - 2023-06-11

### Changed

- Sorted imports with isort

## [0.9.6] - 2023-06-11

### Fixed

- Clear command now functions as expected

### Changed

- Moved Channel ID to .env as CHANNEL

### Removed

- Unused imports

## [0.9.5] - 2023-06-11

### Added

- Delete command to have the bot silently delete messages.
- onmessage check for 'curse' words

## [0.9.4] - 2023-06-11

### Changed

- Names of several minor functions (helpers.timestamp() is now imported simply as timestamp(), for example.)
- Sequencing of some functions, mostly as a matter of formatting

### Fixed

- Minor formatting errors

### Added

- Docstrings to all bot commands
- helpers.py module to contain non-bot commands and events

### Removed

- Unused imports

## [0.9.1] - 2023-04-11

### Added

- say() command
- getLog()
- console messages about current status

### Fixed

- changelog() *should* work now

### Deprecated

- getChangelog()

## [0.9.0]

### Added

- getChangelog()
- !changelog command

## [0.8.5] - 2023-04-11

### Deprecated

- Command online() replaced with status()

### Changed

- Formatted main.py using Black formatter

### Bugfixes

- Removed all log messages containing variables (may not be callable?)

## [0.8.4] - 2023-04-11

### Changed

- Temporarily disable automatic versioning due to possible bug(s)

### Bugfixes

- Removed most log messages to attempt to alleviate error(s)

## [0.8.3] - 2023-04-11

### Added

- .vscode settings directory to .gitignore

## [0.8.2] - 2023-04-11

### Added

- Logging support for many (all?) commands

## [0.8.1] - 2023-04-11

### Fixed

- Semantic version now increments automatically (from this file)

### Added

- getVer() function to source the semantic version info from CHANGELOG.md

## [0.8.0] - 2023-04-11

### Added

- requirements.txt
- Content to README.md

### Changed

- Edited CHANGELOG.md for formatting

## [0.7.7] - 2023-04-11

### Added

- CHANGELOG.md

### Changed

- Updated .gitignore
