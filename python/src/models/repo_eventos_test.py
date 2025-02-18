import pytest

from src.models.repo_eventos import EventosRepo

@pytest.mark.skip("Insert Evento")
def test_insert_evento():
    event_name = 'Evento de Teste'
    event_repo = EventosRepo()
    
    event_repo.insert(event_name)

@pytest.mark.skip("Select Evento")
def test_select_evento():
    event_name = 'Evento de Teste'
    event_repo = EventosRepo()
    
    event = event_repo.select_event(event_name)
    
    assert event.nome == event_name