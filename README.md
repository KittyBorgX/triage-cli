# triage-cli

A CLI for triaging PR's

### Build instructions

```
git clone https://github.com/KittyBorgX/triage-cli.git
cd triage-cli
cp example.env .env # Fill out the .env file
pip install -r requirements.txt
python3 src/main.py
```

### Environment variables

All the environment variables that are required to be set are mentioned in [example.env](./example.env).
The values can either be set in the `.env` file or can be set as system environment variables.

### Roadmap

- [x] GraphQL Github API
- [x] Sorting Pull Requests
- [x] Writing to a backup directory
- [x] Install script
- [ ] Zulip Integration
- [ ] Setup CI
- [ ] Error Messages & Error Handling
- [ ] Better CLI (argparse)
- [ ] Generic API (Not specific to rust-lang/rust)
- [ ] A better project name
- [ ] Modifying GitHub Labels
- [ ] RIIR
