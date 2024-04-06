import json
from app import load_streamlit_updates


def test_load_streamlit_updates():
    """Test the load_streamlit_updates function to ensure it loads data correctly."""
    updates = load_streamlit_updates()
    assert isinstance(updates, dict), "Updates should be a dictionary."
    assert "Highlights" in updates, "Updates should contain 'Highlights'."
