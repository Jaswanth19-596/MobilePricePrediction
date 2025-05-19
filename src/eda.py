import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def univariate_categorical_analysis(df, col):
    print(f"📊 Analyzing Categorical Column: **{col}**")
    print('-' * 50)

    # --- 1. Basic Info ---
    print(f"🔹 Data Type: {df[col].dtype}")
    print(f"🔹 Missing Values: {df[col].isna().sum()} ({df[col].isna().mean()*100:.2f}%)")
    print(f"🔹 Unique Categories: {df[col].nunique(dropna=True)}")
    print()

    # --- 2. Value Counts (with NaNs included) ---
    val_counts = df[col].value_counts(dropna=False)
    val_perc = df[col].value_counts(normalize=True, dropna=False) * 100
    summary = pd.DataFrame({'Count': val_counts, 'Percentage': val_perc.round(2)})
    print("🔹 Category Distribution (including NaNs):")
    print(summary)

    # Replace NaNs with label for plotting
    df_plot = df.copy()

    # Handle categorical column safely
    if pd.api.types.is_categorical_dtype(df_plot[col]):
        if 'Missing' not in df_plot[col].cat.categories:
            df_plot[col] = df_plot[col].cat.add_categories('Missing')

    df_plot[col] = df_plot[col].fillna('Missing')


    # --- 3. Plots ---
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    # Countplot (Bar Plot)
    sns.countplot(data=df_plot, y=col, order=df_plot[col].value_counts().index, palette='Set2', ax=axs[0])
    axs[0].set_title('Category Counts')
    axs[0].set_xlabel('Count')
    axs[0].set_ylabel('')

    # Add count labels to bars
    for p in axs[0].patches:
        width = p.get_width()
        axs[0].text(width + 5, p.get_y() + p.get_height()/2, f'{int(width)}', va='center')

    # Pie Chart (with missing included)
    df_plot[col].value_counts().plot.pie(autopct='%1.1f%%',
                                         colors=sns.color_palette('pastel'),
                                         ax=axs[1],
                                         startangle=90,
                                         wedgeprops=dict(width=0.3, edgecolor='w'))
    axs[1].set_title('Category Proportions')
    axs[1].set_ylabel('')

    plt.tight_layout()
    plt.show()


def univariate_numerical_analysis(df, col):
    print(f"📊 Analyzing Numerical Column: **{col}**")
    print('-' * 50)

    # --- 1. Basic Stats ---
    print(f"🔹 Data Type: {df[col].dtype}")
    print(f"🔹 Missing Values: {df[col].isna().sum()} ({df[col].isna().mean()*100:.2f}%)")
    print(f"🔹 Unique Values: {df[col].nunique()}")
    print()
    print("🔹 Descriptive Statistics (excluding NaNs):")
    print(df[col].describe())

    # --- 2. Outlier Info (IQR method) ---
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print()
    print(f"🔹 Outliers Detected (IQR): {len(outliers)}")
    print(f"    - Lower bound: {lower:.2f}")
    print(f"    - Upper bound: {upper:.2f}")

    # --- 3. Plots ---
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))

    # Histogram + KDE
    sns.histplot(df[col], kde=True, ax=axs[0, 0], color='skyblue')
    axs[0, 0].axvline(df[col].mean(), color='red', linestyle='--', label='Mean')
    axs[0, 0].set_title('Histogram + KDE (excl. missing)')
    axs[0, 0].legend()

    # Boxplot
    sns.boxplot(x=df[col], ax=axs[0, 1], color='lightcoral')
    axs[0, 1].set_title('Boxplot (excl. missing)')

    # Violin plot
    sns.violinplot(x=df[col], ax=axs[1, 0], color='lightgreen')
    axs[1, 0].set_title('Violin Plot (excl. missing)')

    # Missing value bar chart
    missing_counts = df[col].isna().value_counts().rename(index={True: 'Missing', False: 'Present'})
    sns.barplot(x=missing_counts.index, y=missing_counts.values, ax=axs[1, 1], palette=['orange', 'lightblue'])
    axs[1, 1].set_title('Missing vs Present Value Count')
    axs[1, 1].set_ylabel('Count')
    axs[1, 1].set_xlabel('Data Availability')

    for index, value in enumerate(missing_counts.values):
        axs[1, 1].text(index, value + 0.01*max(missing_counts.values), str(value), ha='center', fontweight='bold')

    plt.tight_layout()
    plt.show()

# Before transformation
def plot_before_transformation(df, x, y, order = None):
    sns.barplot(data=df, x = x, y = y, palette='pastel')
    plt.xticks(rotation = 90)
    plt.show()


# After transformation
def plot_after_transformation(df, x, y, order):
    sns.barplot(data=df, x = x, y = y, palette='pastel', order = order)
    plt.xticks(rotation = 90)
    plt.show()


def group_cores(core):
    if core in ['single', 'dual', 'quad']:
        return 'Low_Core'
    elif core in ['hexa', 'octa']:
        return 'Mid_Core'
    else:
        return 'High_Core'


# After Transformation
def transform_camera_features(camera):
    if camera in [0.0, 1.0, 2.0]:
        return 'Less Features'
    elif camera in [3.0, 4.0, 5.0]:
        return 'Medium Features'
    else:
        return 'High Features'

def transform_ram(ram):
    if ram <= 4:
        return '<= 4'
    elif ram <= 8:
        return '6 - 8'
    elif ram <= 16:
        return '8-16'
    return '16+'


def transform_bluetooth_version(version):
   version = int(version)

   if version <= 4:
      return 'Less than 4'

   return version