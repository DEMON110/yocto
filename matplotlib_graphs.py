import matplotlib.pyplot as plt
import csv

def load_metrics():
    """
    Loads performance metrics from the CSV file for visualization.
    """
    metrics = {'Metric': [], 'Stock GCC': [], 'Stock Clang': [], 'All Clang': []}
    with open('metrics.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            metrics['Metric'].append(row['Metric'])
            metrics['Stock GCC'].append(float(row['Stock GCC']))
            metrics['Stock Clang'].append(float(row['Stock Clang']))
            metrics['All Clang'].append(float(row['All Clang']))
    return metrics

def plot_metrics(metrics):
    """
    Generates a line graph comparing performance metrics for different builds.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(metrics['Metric'], metrics['Stock GCC'], label='Stock GCC', marker='o')
    ax.plot(metrics['Metric'], metrics['Stock Clang'], label='Stock Clang', marker='o')
    ax.plot(metrics['Metric'], metrics['All Clang'], label='All Clang', marker='o')

    ax.set_xlabel('Metric')
    ax.set_ylabel('Value')
    ax.set_title('Performance Metrics Comparison')
    ax.legend()

    plt.savefig('performance_metrics.png')
    plt.show()

if __name__ == "__main__":
    metrics = load_metrics()
    plot_metrics(metrics)
