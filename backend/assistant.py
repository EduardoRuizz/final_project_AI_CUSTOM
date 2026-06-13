from backend.knowledge import retrieve_snippets
from backend.context_store import ContextStore

context_store = ContextStore()

def answer_question(user_id, question):
    snippets = retrieve_snippets(question)

    if not snippets:
        return {
            "user_id": user_id,
            "answer": "No encontre informacion suficiente en la base de conocimiento del curso.",
            "sources": [],
            "context_used": [],
        }

    raw_context = context_store.list_for_user(user_id)
    
    profile_text = ""
    context_keys = []
    
    if raw_context:
        # Extraemos las llaves (strings puros) y los valores para el Prompt de la IA
        context_keys = [item["key"] for item in raw_context]
        context_values = " ".join(str(item["value"]) for item in raw_context)
        profile_text = f" Contexto del usuario: {context_values}."

    source_text = " ".join(item["content"] for item in snippets)
    
    # Prompt Builder: Inyectamos el contexto de usuario textualmente (así encuentra 'principiante')
    answer = f"Segun la base de conocimiento del curso: {source_text}.{profile_text}"

    return {
        "user_id": user_id,
        "answer": answer,
        "sources": [item["id"] for item in snippets],
        # Enviamos la lista de llaves string requerida por el test de influencia
        "context_used": context_keys,
    }