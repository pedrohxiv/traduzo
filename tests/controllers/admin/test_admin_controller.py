from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    user = UserModel({
        "name": "admin",
        "level": "admin",
        "token": "token",
    })
    user.save()

    history = HistoryModel({
        "text-to-translate": "House",
        "translate-from": "en",
        "translate-to": "pt",
    })
    history.save()

    response = app_test.delete(f"/admin/history/{history.id}", headers={
      "Authorization": "token",
      "User": "admin",
    })

    assert response.status_code == 204
