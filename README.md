# triage-cli
A CLI for triaging PR's

### Build instructions
```
git clone https://github.com/KittyBorgX/triage-cli.git
cd triage-cli
pip install -r requirements.txt
GITHUB_API_TOKEN=token python3 src/main.py
```

### Roadmap
- [x] GraphQL Github API
- [x] Sorting Pull Requests
- [ ] Writing to a backup directory
- [ ] Error Messages & Error Handling
- [ ] Generic API (Not specific to rust-lang/rust)
- [ ] Zulip Integration
- [ ] Modifying GitHub Labels
- [ ] RIIR