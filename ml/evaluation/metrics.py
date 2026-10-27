from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    silhouette_score,
)


def classification_metrics(
    y_true,
    y_pred,
):

    return {
        "accuracy":
            float(
                accuracy_score(
                    y_true,
                    y_pred,
                )
            ),

        "precision":
            float(
                precision_score(
                    y_true,
                    y_pred,
                    zero_division=0,
                )
            ),

        "recall":
            float(
                recall_score(
                    y_true,
                    y_pred,
                    zero_division=0,
                )
            ),

        "f1":
            float(
                f1_score(
                    y_true,
                    y_pred,
                    zero_division=0,
                )
            ),
    }


def clustering_metrics(
    X,
    labels,
):

    unique_labels = set(labels)

    if len(unique_labels) <= 1:
        return {
            "silhouette": 0.0
        }

    return {
        "silhouette":
            float(
                silhouette_score(
                    X,
                    labels,
                )
            )
    }


def anomaly_auc(
    y_true,
    scores,
):

    return float(
        roc_auc_score(
            y_true,
            scores,
        )
    )