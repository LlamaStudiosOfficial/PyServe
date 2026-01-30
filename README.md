# PyServe

PyServe is a lightweight, local‑network file sharing server with a clean web dashboard, per‑device upload identification, secure delete passwords, and a modern UI.  
It runs entirely on LAN so it does ***not*** go to any servers.

> [!CAUTION]
> PyServe is intended for LAN use *only*.
> Using PyServe on a public network could expose your device to **malware**.

---

## ✨ Features

- 📁 File Upload & Download
- 🔐 Secure Delete System
> Every uploaded file receives a **unique delete password**:
> Password shown **only once** to the uploader  
> Required to delete the file  
> Prevents other users on the network from deleting your uploads  

### 🖥️ Per‑Device Identification
Each device is assigned a persistent ID:
```
<platform>-<random>.hidden
```
Your own uploads are highlighted in **blue**.

---

## 🚀 Getting Started

> [!TIP]
> If you want to get started fast, use the pre-builts from the releases page and run the **executable** in a folder.
> The folder `assets` ***must*** exsist with a meta.json with the folowing contense: ```{}```


### 📦 1. Install dependencies
PyServe requires these dependencies:
- Flask

Install the dependencies by running this command:
```bash
pip install flask
```

### 📂 2. Create nesseserry files/folders

Folder structure:
```
MyFolder/
assets/
├─ meta.json
app.py
```

> [!IMPORTANT]
> `meta.json` ***must*** contain this contents:
> `{}`



### 🖥️ 3. Run the server

```bash
python app.py
```

### 🚪 4. Access PyServe

Open the **address shown in the console**.Look for: `Running on http://`. The address is usually `http://<your-local-ip>:5000`.
To find you ip run the command `ipconfig`.

---

**Any device on the** ***same*** **Wi‑Fi network** can access the **PyServe server**.
### 🔒 Security:
When a file is uploaded, the client sends its device ID.
The server generates a password to stop abuse by deleting each others' files.
This prevents unauthorized deletion on **shared PyServe Server**.

### 📝 License

PyServe is licensed under the **MIT License**.
