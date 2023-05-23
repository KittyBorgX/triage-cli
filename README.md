# triage-cli

A CLI for triaging PR's

## Usage:

```
triage-cli: A command line interface for triaging pull requests.

Usage: triage-cli [OPTIONS]

Options:
-pz, --post-to-zulip         Post the report on completion to zulip
-d, --details                Add additional details like createdTime to the report
-o, --output [FILENAME]      Paste the report in the specified file
-p, --print                  Print the report after triaging
-h, --help                   Display this help message
```

## CLI Options:

- `-pz` or `--post-to-zulip` : Posts the generated report after completion (on sending `q` as a query in the `PR num` field) to the `t-release/triage` stream with the topic name as the current date. This requires the `$ZULIP_EMAIL_ID` and `$ZULIP_API_KEY` environment variables to be set, else will error out.

- `-d` or `--details` : Adds additional details to the pull request in the form of a clickable dropdown menu. The various details that are added into the dropdown menu are - `Title`, `Last Updated at`, `Created at`, `Labels`, `Status`.

- `-p` or `--print` : Prints the report as raw markdown to the `stdout` instead of saving to a file.

## Build instructions

1. Run these commands:

   ```
   git clone https://github.com/KittyBorgX/triage-cli.git
   cd triage-cli
   chmod +x install.py
   ./install.py
   ```

2. Fill up the created `.env` file with the appropriate environment variables or set them as environment variables in your current shell

Or manually:

1. Run the following commands:

   ```
   git clone https://github.com/KittyBorgX/triage-cli.git
   cd triage-cli
   pip install -r requirements.txt
   cp example.env .env
   ```

2. Fill up the created `.env` file with the appropriate environment variables or set them as environment variables in your current shell

3. Get your current working directory by running `pwd`

4. Open your shellrc file (example: `$HOME/.zshrc`) and add the following:

   ```
   alias tcli="python {cwd}/src/main.py"
   ```

- And replace `{cwd}` with the output of `pwd`. example:

  ```
  alias tcli="python /home/kitty/triage-cli/src/main.py"
  ```

5. Re-load your current shell or run `source $HOME/.zshrc` if you're in the zsh shell or `$source $HOME/.bashrc`

## Environment variables

All the environment variables that are required to be set are mentioned in [example.env](./example.env).
The values can either be set in the `.env` file or can be set as system environment variables.

## Roadmap ()

- [x] GraphQL Github API
- [x] Sorting Pull Requests
- [x] Writing to a backup directory
- [x] Zulip Integration
- [x] Install script
- [x] Better CLI
- [x] Error Messages & Error Handling
- [x] Documentation
- [ ] Modifying GitHub Labels
- [ ] Unit test
- [ ] Setup CI
- [ ] RIIR?
