# triage-cli

A CLI for triaging PR's

### Build instructions

```
git clone https://github.com/KittyBorgX/triage-cli.git
cd triage-cli
cp example.env .env # Fill out the .env file
cargo run 
```

### Environment variables

All the environment variables that are required to be set are mentioned in [example.env](./example.env).
The values can either be set in the `.env` file or can be set as system environment variables.

### Roadmap (riir)

- [ ] GraphQL Github API
- [ ] Sorting Pull Requests
- [ ] Writing to a backup directory
- [ ] Install script
- [ ] Zulip Integration
- [ ] Setup CI
- [ ] Error Messages & Error Handling
- [ ] Better CLI
- [ ] Generic API (Not specific to rust-lang/rust)
- [ ] A better project name
- [ ] Modifying GitHub Labels
- [ ] RIIR?
