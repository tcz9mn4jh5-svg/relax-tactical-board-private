import streamlit as st


BOARD_URL = "/app/static/tactical_board/index.html"

st.set_page_config(
    page_title="ReLax Tactical Board",
    page_icon="🥍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .main .block-container {
        max-width: none;
        padding: 0.5rem 0.7rem 1rem;
    }
    [data-testid="stSidebar"],
    [data-testid="stHeader"] {
        display: none;
    }
    .board-launch {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        margin: 0 0 8px;
        padding: 10px 14px;
        border-radius: 12px;
        background: #0f2747;
        color: white;
    }
    .board-launch strong {
        font-size: 18px;
    }
    .board-launch a {
        display: inline-block;
        padding: 9px 13px;
        border-radius: 9px;
        background: #0369a1;
        color: white;
        text-decoration: none;
        font-weight: 800;
        white-space: nowrap;
    }
    </style>
    <div class="board-launch">
        <strong>ReLax Tactical Board</strong>
        <a href="/app/static/tactical_board/index.html" target="_blank">
            全画面・ホーム画面追加用に開く ↗
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.iframe(BOARD_URL, height=980, width="stretch", tab_index=0)
