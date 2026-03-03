class QueueManager:
    def __init__(self):
        self._items = []
        self._pending_count = 0
        self._pending_or_downloading_count = 0

    def _bump_counts_for_status(self, status, delta):
        if status == "pending":
            self._pending_count += delta
            self._pending_or_downloading_count += delta
        elif status == "downloading":
            self._pending_or_downloading_count += delta

    def add(self, url, mode, options=None):
        item = {
            "url": str(url),
            "status": "pending",
            "title": str(url),
            "mode": str(mode),
            "options": dict(options or {}),
            "error_message": "",
            "progress": 0.0,
        }
        self._items.append(item)
        self._bump_counts_for_status("pending", 1)
        return len(self._items) - 1

    def remove(self, index):
        if index < 0 or index >= len(self._items):
            return False

        status = self._items[index]["status"]
        if status not in {"pending", "finished", "error"}:
            return False

        self._bump_counts_for_status(status, -1)
        self._items.pop(index)
        return True

    def clear_finished(self):
        before = len(self._items)
        self._items = [
            item for item in self._items
            if item["status"] not in {"finished", "error", "cancelled"}
        ]
        self._pending_count = sum(1 for item in self._items if item["status"] == "pending")
        self._pending_or_downloading_count = sum(
            1 for item in self._items if item["status"] in {"pending", "downloading"}
        )
        return len(self._items) != before

    def clear_all(self):
        if not self._items:
            return False
        self._items = []
        self._pending_count = 0
        self._pending_or_downloading_count = 0
        return True

    def get_next_pending(self):
        for index, item in enumerate(self._items):
            if item["status"] == "pending":
                return index, item
        return None, None

    def get_all(self):
        return self._items

    def count_pending(self):
        return self._pending_count

    def count_pending_or_downloading(self):
        return self._pending_or_downloading_count

    def is_empty(self):
        return len(self._items) == 0

    def update_status(self, index, status, error_message=""):
        if index < 0 or index >= len(self._items):
            return False
        current_status = self._items[index]["status"]
        new_status = str(status)

        if current_status != new_status:
            self._bump_counts_for_status(current_status, -1)
            self._bump_counts_for_status(new_status, 1)

        self._items[index]["status"] = new_status
        self._items[index]["error_message"] = str(error_message)
        return True

    def cancel_all_pending(self):
        cancelled = 0
        for item in self._items:
            if item["status"] == "pending":
                item["status"] = "cancelled"
                cancelled += 1

        if cancelled:
            self._pending_count -= cancelled
            self._pending_or_downloading_count -= cancelled

        return cancelled

    def update_title(self, index, title):
        if index < 0 or index >= len(self._items):
            return False
        self._items[index]["title"] = str(title)
        return True

    def update_progress(self, index, progress):
        if index < 0 or index >= len(self._items):
            return False
        self._items[index]["progress"] = float(max(0.0, min(100.0, progress)))
        return True
