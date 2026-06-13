"""Base placeholder for student implementation."""
import os
import json

class ContextStore:
    def __init__(self, storage_path="data/user_context.json"):
        self.storage_path = storage_path
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def _load_data(self):
        with open(self.storage_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_data(self, data):
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def save(self, user_id, key, value):
        data = self._load_data()
        if user_id not in data:
            data[user_id] = {}
        data[user_id][key] = value
        self._save_data(data)
        return {key: value}

    def list_for_user(self, user_id):
        """Devuelve el contexto completo del usuario en una estructura serializable limpia."""
        data = self._load_data()
        user_context = data.get(user_id, {})
        
        # Retornamos una lista estructurada con formato de objeto clave-valor explícito
        # Evita errores de hash en validadores estrictos de API
        return [{"key": k, "value": v} for k, v in user_context.items()]