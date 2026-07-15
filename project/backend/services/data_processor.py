from typing import Any, Optional
from datetime import datetime
import json


class DataProcessor:
    @staticmethod
    def merge_responses(responses: list[dict]) -> dict:
        merged = {"sources": [], "data": [], "fetched_at": datetime.utcnow().isoformat()}
        for response in responses:
            merged["sources"].append(response.get("source", "unknown"))
            data = response.get("data", {})
            if isinstance(data, dict):
                merged["data"].append(data)
            elif isinstance(data, list):
                merged["data"].extend(data)
        return merged

    @staticmethod
    def remove_duplicates(items: list[dict], key: str = "id") -> list[dict]:
        seen = set()
        unique = []
        for item in items:
            val = item.get(key)
            if val and val not in seen:
                seen.add(val)
                unique.append(item)
        return unique

    @staticmethod
    def clean_nulls(data: dict) -> dict:
        if isinstance(data, dict):
            return {k: DataProcessor.clean_nulls(v) for k, v in data.items() if v is not None}
        elif isinstance(data, list):
            return [DataProcessor.clean_nulls(item) for item in data if item is not None]
        return data

    @staticmethod
    def convert_timestamps(data: dict, format: str = "iso") -> dict:
        if isinstance(data, dict):
            return {k: DataProcessor.convert_timestamps(v, format) for k, v in data.items()}
        elif isinstance(data, list):
            return [DataProcessor.convert_timestamps(item, format) for item in data]
        return data

    @staticmethod
    def normalize_json(data: Any) -> dict:
        if isinstance(data, str):
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                return {"raw": data}
        return data

    @staticmethod
    def validate_data(data: dict, required_fields: list[str]) -> tuple[bool, list[str]]:
        errors = []
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        return len(errors) == 0, errors

    @staticmethod
    def transform_javascript(items: list[dict], transform_fn) -> list[dict]:
        return [transform_fn(item) for item in items]
