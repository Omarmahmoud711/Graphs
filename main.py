from GUI import MatrixEditor

if __name__ == "__main__":
    Vn=int(input("Enter the number of Vertices: "))
    app = MatrixEditor(Vn)
    app.mainloop()