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


### 🖥️ Per‑Device Identification
Each device is assigned a persistent ID:
```
<platform>-<random>.hidden
```
Your own uploads are highlighted in **blue**.
> [!TIP]
> If you want to get started fast, use the pre-builts from the releases page and run the **executable** in a folder.
> Anything in the **assets** folder will be loaded on the server.
<details>

<summary>Installing PyServe</summary>

## 🚀 Getting Started

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

`meta.json` ***must*** contain this contents by default: 
```json
{}
```




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
The server ***only*** lets the person who uploaded the file delete it.
This prevents unauthorized deletion on **shared PyServe Server**.
</details>

### 📝 License

PyServe is licensed under the **MIT License**.
