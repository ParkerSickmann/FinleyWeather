# FinleyWeather

A Python application for working with weather data.

This guide will walk you through setting up the project from a blank Windows install (no Python, no VS Code, nothing installed yet).

---

## 1. Install Python

1. Go to [Python Downloads for Windows](https://www.python.org/downloads/windows/).
2. Download the latest stable **Python 3.x (64-bit)** installer.
3. Run the installer. **Important:** check the box that says **“Add Python to PATH”**.
4. Complete the installation.

To verify installation, open **Command Prompt** (search *cmd* in the Start menu) and run:

```bash
python --version
pip --version
```

Both should return version numbers.

---

## 2. Install Visual Studio Code (optional but recommended)

1. Download VS Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Install with default options (you can check “Add to PATH” and “Open with Code” if offered).
3. Launch VS Code, then **install the Python extension** when prompted.

---

## 3. Download the Project

### Option A: Using Git (recommended)

1. Install Git: [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Open Command Prompt, then run:

```bash
git clone https://github.com/ParkerSickmann/FinleyWeather.git
cd FinleyWeather
```

### Option B: Without Git

1. Go to the [GitHub repo](https://github.com/ParkerSickmann/FinleyWeather).
2. Click **Code → Download ZIP**.
3. Extract the ZIP and open the folder in Command Prompt:

```bash
cd path\to\FinleyWeather
```

---

## 4. Install Required Libraries

Make sure you’re inside the `FinleyWeather` folder, then run:

```bash
pip install -r requirements.txt
```

This installs all the Python libraries the project needs.

If `requirements.txt` is missing, install libraries individually (for example):

```bash
pip install requests
```

---

## 5. Run the Project

Once dependencies are installed, run the main script. For example, if the entry file is `main.py`:

```bash
python main.py
```

Check your repo for the correct filename (`main.py`, `app.py`, etc.).

---

## 6. Troubleshooting

* If `python` isn’t recognized, log out and back in, or reinstall ensuring **“Add to PATH”** was checked.

* If `pip` errors, try upgrading it:

  ```bash
  python -m pip install --upgrade pip
  ```

* If libraries fail to install, check `requirements.txt` and install them one at a time.
              
