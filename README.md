# TelegramForward
Want to auto forward telegram group message to channels?

# How to use?
1. Install Packages
```bash
pip install .devcontainer/requirements.txt
```
2. Go to [Telegram.org](my.telegram.org), And get API_ID, API_HASH
3. Make Env File (.env), xxxxxx is yours
```env
API_ID=xxxxxxx
API_HASH=xxxxxx
```
4. Get dialogs id via list_dialogs method
5. Fill the source and target dialog.
6. Run script
```bash
python main.py
```
