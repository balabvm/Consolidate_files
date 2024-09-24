import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to consolidate CSV files
def consolidate_csv_files(folder_path):
    df_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            df_list.append(df)
    if df_list:
        consolidated_df = pd.concat(df_list, ignore_index=True)
        output_file = os.path.join(folder_path, 'consolidated_data.csv')
        consolidated_df.to_csv(output_file, index=False)
        messagebox.showinfo("Success", f'Consolidated CSV file saved to {output_file}')
    else:
        messagebox.showwarning("No CSV Files", "No CSV files found in the selected folder.")

# Function to consolidate Excel files
def consolidate_excel_files(folder_path):
    df_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)
            df_list.append(df)
    if df_list:
        consolidated_df = pd.concat(df_list, ignore_index=True)
        output_file = os.path.join(folder_path, 'consolidated_data.xlsx')
        consolidated_df.to_excel(output_file, index=False)
        messagebox.showinfo("Success", f'Consolidated Excel file saved to {output_file}')
    else:
        messagebox.showwarning("No Excel Files", "No Excel files found in the selected folder.")

# Function to handle Excel button click
def handle_excel_consolidation():
    folder_path = filedialog.askdirectory()
    if folder_path:
        confirm = messagebox.askyesno("Confirmation", "Are the headers in all files the same?")
        if confirm:
            consolidate_excel_files(folder_path)
        else:
            messagebox.showinfo("Aborted", "Please ensure all files have the same headers and try again.")

# Function to handle CSV button click
def handle_csv_consolidation():
    folder_path = filedialog.askdirectory()
    if folder_path:
        confirm = messagebox.askyesno("Confirmation", "Are the headers in all files the same?")
        if confirm:
            consolidate_csv_files(folder_path)
        else:
            messagebox.showinfo("Aborted", "Please ensure all files have the same headers and try again.")

# Create the tkinter root window
root = tk.Tk()
root.title("Data Consolidation")

# Set window size
root.geometry("300x150")

# Create buttons for Excel and CSV consolidation
excel_button = tk.Button(root, text="Excel Files Consolidation", width=20, height=2, command=handle_excel_consolidation)
csv_button = tk.Button(root, text="CSV Files Consolidation", width=20, height=2, command=handle_csv_consolidation)

# Place the buttons in the window
excel_button.pack(pady=10)
csv_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
