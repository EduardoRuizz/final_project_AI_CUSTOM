"""Base placeholder for student implementation."""
import os
import json

class ContextStore:
    def __init__(self, storage_path="data/user_context.json"):
        self.storage_path = storage_path
        # Asegura de forma dinámica que exista la carpeta data/ en la raíz
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        # Si el archivo JSON de persistencia no existe, lo inicializa como un diccionario vacío
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def _load_data(self):
        """Método auxiliar interno para leer el archivo de persistencia JSON."""
        with open(self.storage_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_data(self, data):
        """Método auxiliar interno para escribir en el archivo de persistencia JSON."""
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def save(self, user_id, key, value):
        """Guarda o actualiza una clave-valor en el contexto del usuario."""
        data = self._load_data()
        if user_id not in data:
            data[user_id] = {}
        
        data[user_id][key] = value
        self._save_data(data)
        return {key: value}

    def list_for_user(self, user_id):
        """Devuelve el contexto completo del usuario en un formato de lista estructurada."""
        data = self._load_data()
        user_context = data.get(user_id, {})
        
        # Se transforma el diccionario {key: value} en una lista de objetos [{"key": k, "value": v}]
        # para garantizar la compatibilidad estricta con las aserciones del contrato de pruebas.
        return [{"key": k, "value": v} for k, v in user_context.items()]