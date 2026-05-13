"""Loading module for verifying and using data science libraries."""


def main() -> None:
    """Check library dependencies and run a basic data analysis."""
    print(
        "\nLOADING STATUS: Loading programs..."
        "\n\nChecking dependencies...\n"
    )
    try:
        import pandas as pd
    except ImportError:
        print("[KO] Failed to load pandas library.")
        exit(1)
    else:
        print(
            f"[ok] pandas ({pd.__version__})"
            " - Data manipulation ready."
        )
    try:
        import requests
    except ImportError:
        print("[KO] Failed to load requests library.")
        exit(1)
    else:
        print(
            f"[ok] requests ({requests.__version__})"
            " - HTTP requests ready."
        )
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("[KO] Failed to load matplotlib library.")
        exit(1)
    else:
        print(
            f"[ok] matplotlib ({plt.matplotlib.__version__})"
            " - Visualization ready."
        )
    try:
        import numpy as np
    except ImportError:
        print("[KO] Failed to load numpy library.")
        exit(1)
    else:
        print(
            f"[ok] numpy ({np.__version__})"
            " - Numerical computing ready."
        )

    print("\nAnalyzing Matrix data...")
    data = pd.DataFrame(
        np.random.randn(1000, 3), columns=["A", "B", "C"]
    )

    print("Processing 1000 data points...")
    _ = data.describe()

    print("Generating visualization...")
    fig, ax = plt.subplots()
    data.plot(ax=ax, title="Matrix Analysis")
    plt.tight_layout()

    print("Analysis complete!")
    fig.savefig("matrix_analysis.png")
    plt.close(fig)
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
