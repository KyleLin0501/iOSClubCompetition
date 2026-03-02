# 🚀 2025 iOS App 登場時刻 - 競賽管理系統

本專案為 **iOS Club** 舉辦之「2025 創新應用競賽」的官方系統，包含前端形象展示頁面以及整合 Firebase 的自動化報名管理後台。

---

## 📂 檔案結構說明

| 檔案名稱 | 說明 | 技術棧 |
| :--- | :--- | :--- |
| `index.html` | **競賽入口首頁**。展示競賽宗旨、時程、評分標準及入圍名單。 | Tailwind CSS |
| `registration.html` | **報名與管理系統**。含登入、隊伍編輯、隊員增減及 PDF 上傳功能。 | Bootstrap 5.3, Firebase |

---

## 🔥 Firebase 後端架構

本專案採用 **Firebase 11.6.1 (Modular SDK)**。後續維護者請務必理解以下配置：

### 1. 專案配置 (Firebase Config)
在 `registration.html` 中，金鑰透過 Django 模板變數 `{{ FIREBASE_CONFIG }}` 動態注入。
> **注意：** 若要離線測試或遷移專案，請手動替換為 Firebase Console 提供的 JSON 配置物件。

### 2. Firestore 資料路徑 (Database)
為了落實結構化管理，資料儲存遵循以下路徑：
`artifacts / {projectId} / users / {uid} / teamData / profile`

* **artifacts**: 頂層集合 (Collection)。
* **{projectId}**: 對應 Firebase Project ID 的文件 (Document)。
* **users**: 使用者集合。
* **profile**: 儲存隊伍核心資料的文件，欄位包含：
    * **隊長資訊**：姓名、學號、系級、Line ID 等。
    * **隊員陣列 (members Array)**：儲存 1-3 名隊員的物件資訊。
    * **作品資訊**：名稱、300 字概述、企劃書 (Storage) 連結。

### 3. Authentication (身份驗證)
* **一般使用者**：以 Email 作為帳號登入。登入後僅能存取屬於自己 `uid` 下的資料路徑。
* **管理員 (Admin)**：
    * **固定帳號**：`admin@gmail.com`
    * **特殊權限**：登入後會觸發 `collectionGroup` 查詢，可跨使用者讀取所有隊伍的報名資訊，並具備編輯所有隊伍資料的最高權限（不受截止日期限制）。

### 4. Storage (檔案儲存)
* **儲存路徑**：`artifacts / {projectId} / users / {uid} / proposals / {fileName}`
* **邏輯**：接收前端上傳的 PDF 檔案，成功後產生的 `DownloadURL` 會自動回寫至 Firestore 的 `proposalURL` 欄位。

---

## ⚠️ 安全警告：禁止將 Firebase 憑證傳至 GitHub

為了保護資料庫安全，**絕對禁止**將包含 API Key 的設定檔或金鑰上傳至公開的 GitHub 儲存庫。

### 1. 為什麼不能上傳？
* **資料外洩**：一旦 `GoogleService-Info.plist` 或包含 `firebaseConfig` 的程式碼公開，任何人都可以利用這些金鑰存取你的 Firestore 資料庫與 Storage 檔案。
* **額度盜用**：惡意攻擊者可能利用你的憑證大量呼叫 Firebase 服務，導致你的專案產生高額費用或被停權。

### 2. 如何保護憑證？
本專案使用以下機制保護隱私資料：

* **使用 .gitignore**：
  在專案根目錄下建立 `.gitignore` 檔案，並加入以下內容，確保 Git 忽略這些敏感檔案：
  ```text
  # Firebase 敏感檔案
  GoogleService-Info.plist
  
  # Django 環境變數
  .env
  local_settings.py

---

## 💻 前端技術細節

### 1. 響應式與樣式規範
* **首頁 (`index.html`)**：使用 **Tailwind CSS**，內建滾動平滑 (`scroll-smooth`) 與自定義品牌漸層文字 (`.text-gradient-special`)。
* **報名頁 (`registration.html`)**：使用 **Bootstrap 5.3**，便於快速建構複雜表單、響應式表格與 Modal 彈出視窗。

### 2. 關鍵邏輯處理

#### 🛑 截止時間限制
系統預設截止時間為 `2025-12-08 00:00:00`。
```javascript
const deadline = new Date('2025-12-08T00:00:00+08:00');
// 邏輯：若 (當前時間 > deadline)，系統會自動鎖定所有 Input 欄位並隱藏「儲存」按鈕。
