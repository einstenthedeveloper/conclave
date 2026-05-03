import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

SESSIONS_DIR = Path(__file__).parent / "workspace" / "sessions"
SESSIONS_DIR.mkdir(parents=True, exist_ok=True)

LAUNCH_ARGS = ["--disable-dev-shm-usage", "--no-sandbox", "--disable-gpu"]

_playwright = None
_browser: Browser = None
_context: BrowserContext = None
_page: Page = None


def _ensure_browser():
    global _playwright, _browser, _context, _page
    if _page and not _page.is_closed():
        return
    if _playwright is None:
        _playwright = sync_playwright().start()
    if _browser is None or not _browser.is_connected():
        _browser = _playwright.chromium.launch(
            headless=False,
            slow_mo=400,
            args=LAUNCH_ARGS,
        )
    if _context is None:
        _context = _browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        )
    _page = _context.new_page()


def session_save(name: str) -> dict:
    _ensure_browser()
    path = SESSIONS_DIR / f"{name}.json"
    cookies = _context.cookies()
    path.write_text(json.dumps(cookies, indent=2))
    return {"ok": True, "path": str(path)}


def session_load(name: str) -> dict:
    global _context, _page
    path = SESSIONS_DIR / f"{name}.json"
    if not path.exists():
        return {"ok": False, "error": "SESSION_EXPIRED", "detail": "session file not found"}
    if _playwright is None:
        _ensure_browser()
    if _browser is None or not _browser.is_connected():
        _ensure_browser()
    _context = _browser.new_context(
        viewport={"width": 1280, "height": 900},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    )
    cookies = json.loads(path.read_text())
    _context.add_cookies(cookies)
    _page = _context.new_page()
    return {"ok": True, "session": name}


def browser_navigate(url: str, timeout: int = 60000) -> dict:
    _ensure_browser()
    _page.goto(url, wait_until="domcontentloaded", timeout=timeout)
    time.sleep(2)
    return {"ok": True, "title": _page.title(), "url": _page.url}


def browser_click(selectors: list[str], timeout: int = 8000) -> dict:
    _ensure_browser()
    for sel in selectors:
        try:
            _page.locator(sel).first.click(timeout=timeout)
            time.sleep(0.8)
            return {"ok": True, "matched": sel}
        except Exception:
            continue
    return {"ok": False, "error": f"no selector matched from: {selectors}"}


def browser_type(selectors: list[str], text: str, delay: int = 40) -> dict:
    _ensure_browser()
    for sel in selectors:
        try:
            _page.locator(sel).first.click(timeout=5000)
            _page.keyboard.type(text, delay=delay)
            return {"ok": True, "matched": sel}
        except Exception:
            continue
    return {"ok": False, "error": f"no selector matched from: {selectors}"}


def browser_upload(selectors: list[str], filepath: str) -> dict:
    _ensure_browser()
    for sel in selectors:
        try:
            with _page.expect_file_chooser(timeout=8000) as fc_info:
                _page.locator(sel).first.click(timeout=5000)
            fc_info.value.set_files(filepath)
            time.sleep(2)
            return {"ok": True, "matched": sel, "file": filepath}
        except Exception:
            continue
    return {"ok": False, "error": f"upload failed, no selector matched from: {selectors}"}


def browser_screenshot(path: str) -> dict:
    _ensure_browser()
    _page.screenshot(path=path)
    return {"ok": True, "path": path}


def browser_wait_for(selectors: list[str], timeout: int = 10000) -> dict:
    _ensure_browser()
    for sel in selectors:
        try:
            _page.locator(sel).first.wait_for(timeout=timeout)
            return {"ok": True, "found": sel}
        except Exception:
            continue
    return {"ok": False, "error": "timeout", "selectors_tried": selectors}


def browser_get_text(selector: str) -> dict:
    _ensure_browser()
    try:
        text = _page.locator(selector).first.inner_text(timeout=5000)
        return {"ok": True, "text": text}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def browser_close():
    global _playwright, _browser, _context, _page
    try:
        if _browser:
            _browser.close()
        if _playwright:
            _playwright.stop()
    except Exception:
        pass
    _playwright = _browser = _context = _page = None
