# 🏗️ Mumbai Civil Works Contractor Website & API

A beautiful, high-performance, and mobile-optimized web application for a Civil Construction and Renovation business based in Mumbai. Built to be lightweight, SEO-friendly, and integrated with a **FastAPI** backend server for dynamic photo uploads.

## 📞 Business Contact Details
*   **Service Area:** All Over Mumbai (Andheri, Bandra, Thane, Navi Mumbai, etc.)
*   **Offer:** Affordable Civil Work with a **100% Free Site Visiting** Guarantee.
*   **Mobile Number:** +91 7757838070 (Supports Calls & WhatsApp)

---

## 🚀 Project Features
1. **Modern UI Design:** Styled cleanly using Tailwind CSS with professional engineering-focused visual accents.
2. **Advanced SEO Ready:** Built-in semantic meta descriptions, headers, and keyword structures optimized specifically to rank on Google search for *"Civil Contractors in Mumbai"*.
3. **Smart Mobile Call Triggers:** Sticky action buttons at the base of smaller touch screens for one-click calling or WhatsApp messaging.
4. **FastAPI Image Processor:** Includes an industrial-standard API handling photo selections straight from construction sites.

---

## 📁 Repository Structure
The repository consists of exactly 3 core files running at the root directory level:
*   `index.html` - The static frontend webpage user-interface (Deployed to GitHub Pages).
*   `main.py` - The FastAPI Python backend script responsible for receiving file uploads.
*   `requirements.txt` - Lists system library prerequisites required by free Python cloud hosting.

---

## 🛠️ Step-by-Step Deployment Instructions

### Part 1: Hosting the Frontend (100% Free on GitHub Pages)
1. Go to this repository's **Settings** tab.
2. Click on **Pages** located in the left sidebar menu.
3. Under the **Build and deployment** section, look for *Source* and ensure it is set to "Deploy from a branch".
4. Toggle the Branch drop-down option from *None* to **`main`** (or `master`) and keep the folder path root (`/`).
5. Click **Save**. Within 1–2 minutes, your website will be live at: `https://<your-username>.github.io/<repository-name>/`

### Part 2: Hosting the Backend (Free Python Server on Render.com)
Because GitHub Pages only processes static client-side structures, your `main.py` Python code must be hosted on an active cloud server pipeline:
1. Create a free account at **[Render.com](https://render.com)**.
2. Click **New +** on your dashboard and select **Web Service**.
3. Connect your GitHub account and choose this repository (`mumbai-civil-contractors`).
4. Apply the following configuration settings:
    *   **Runtime:** `Python 3`
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click **Deploy Web Service**.

### Part 3: Connecting Both Systems Together
Once your Render web service status shows as successfully deployed:
1. Copy the custom web link provided by Render (e.g., `https://onrender.com`).
2. Go back to your GitHub repository, open **`index.html`**, and click the edit pencil icon.
3. Scroll near the bottom area (around line 133) and update the `BACKEND_URL` variable:
   ```javascript
   const BACKEND_URL = "https://onrender.com";
   ```
4. Save (**Commit Changes**). Now when you upload a photo from your phone, it will seamlessly cross-communicate directly with your live Python cloud database!

---
*Developed as a high-conversion, professional lead generator for construction businesses in Mumbai.*
