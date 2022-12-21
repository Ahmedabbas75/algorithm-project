# importing libraries
from variable import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


# class mainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set vertices zero value,number of vertices
        self.vertices = 0

        # create empty list to store graph
        self.graph = []

        # set item zero value,we need it in binary search
        self.item = 0

        # add title to window
        self.setWindowTitle("Algorithms app")

        # setting window icon
        self.setWindowIcon(QIcon("C:\\Users\\ahmed abbas\\Desktop\\my project\\sorting\\pictures\\Window"))

        # setting window size
        self.resize(800,400)

        # call style window methods
        self.style_Mwindow()

        # displying window
        self.show()

     # style of window
    def style_Mwindow(self):

        # add menues in window 
        Menus = self.menuBar()

        # add sections  in window
        manage = Menus.addMenu("Manage app")
        T_menu = Menus.addMenu("Go")
        view_menu = Menus.addMenu("View")

        # add description to manage sections and icon
        about = manage.addAction("About")
        about.setIcon(QIcon("C:\\Users\\ahmed abbas\\Desktop\\my project\\sorting\\pictures\\about"))
        help = manage.addAction("Help")
        help.setIcon(QIcon("C:\\Users\\ahmed abbas\\Desktop\\my project\\sorting\\pictures\\help"))
        descrip = manage.addAction("description")
        descrip.setIcon(QIcon("C:\\Users\\ahmed abbas\\Desktop\\my project\\sorting\\pictures\\description"))

        # add action if clecked of item
        about.triggered.connect(self.about)
        help.triggered.connect(self.help)
        descrip.triggered.connect(self.description)

        # add array area and description it
        self.Label = QLabel("<b>Array number : </b>",self)
        self.Label.move(20,65)
        self.Label.resize(150,40)
        self.Label.setStyleSheet("font-size:15px")
        self.Arr_area = QTextEdit(self)
        self.Arr_area.move(20,100)
        self.Arr_area.resize(760,100)
        self.Arr_area.setStyleSheet("font-size:15px")
        self.Arr_area.setToolTip("enter array number like 1,2,3,4,5")

        # add Insertion sort button
        self.button_Insertion = QPushButton("Insertion sort",self)
        self.button_Insertion.move(50,250)
        self.button_Insertion.setStyleSheet("border-radius:8px;font-size:15px;bacKground:#344D67;color:white;")
        self.button_Insertion.clicked.connect(self.Insertion_sort)

        # add Selection sort button
        self.button_selection = QPushButton("Selection sort",self)
        self.button_selection.move(250,250)
        self.button_selection.setStyleSheet("border-radius:8px;font-size:15px;bacKground:#344D67;color:white;")
        self.button_selection.clicked.connect(self.Selection_sort)

        # add kruskal’s algorithm button
        self.button_kruskal = QPushButton("kruskal’s algorithm",self)
        self.button_kruskal.resize(130,32)
        self.button_kruskal.move(435,250)
        self.button_kruskal.setStyleSheet("border-radius:8px;font-size:15px;bacKground:#344D67;color:white;")
        self.button_kruskal.clicked.connect(self.add_vertices)

        # add Binary search button
        self.button_binarysersh = QPushButton("Binary search",self)
        self.button_binarysersh.move(650,250)
        self.button_binarysersh.setStyleSheet("border-radius:8px;font-size:15px;bacKground:#344D67;color:white;")
        self.button_binarysersh.clicked.connect(self.showDialog)

        # add Exit button
        self.button_exit = QPushButton("Exit",self)
        self.button_exit.move(340,350)
        self.button_exit.setStyleSheet("border-radius:8px;font-size:15px;bacKground:#344D67;color:white;")
        self.button_exit.clicked.connect(self.Q_exit)


    # window to tell ather who am i 
    def about(self):
        QMessageBox.about(self,"Who am i",about_D)
    
    # window to tell ather how to use app
    def help(self):
        QMessageBox.about(self,"how to use program",help_D)
    
    # window to description what app do and how function work
    def description(self):
        QMessageBox.about(self,"What is our program",descri_D)

    # asking user about number they want to search it
    def showDialog(self):
        text, ok = QInputDialog.getText(self, "asking key", "Enter number want to search it:")
        if ok:
            self.item = int(text)
            self.B_search()

    # asking user about number of vertices
    def add_vertices(self):
        number, ok = QInputDialog.getText(self, "asking vertices", "Enter number of vertices : ")
        if ok:
            self.vertices = int(number)
            self.add_edge() # call add edge function 
    
    # function to add an edge to graph
    def add_edge(self):
        while True:
            text, ok = QInputDialog.getText(self, "add edges to graph", "Enter node1, node2 and weighte like 1,2,3 :")
            if ok:
                self.graph.append([int(i) for i in text.split(",")])
            else:break
        self.kruskal() # call kruskal function 

    # unction to find set of an element item in graph
    def search_ingraph(self, parent, item_ingraph):
        if parent[item_ingraph] == item_ingraph:
            return item_ingraph
        return self.search_ingraph(parent, parent[item_ingraph])

    # function that does union of two sets of x and y
    def apply_union(self, parent, rank, x, y):
        xroot = self.search_ingraph(parent, x)
        yroot = self.search_ingraph(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #function to construct MST using Kruskal's algorithm
    def kruskal(self):
        sub_graph = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while e < self.vertices - 1:
            node1, node2, w = self.graph[i]
            i = i + 1
            search_node1 = self.search_ingraph(parent, node1)
            search_node2 = self.search_ingraph(parent, node2)
            if search_node1 != search_node2:
                e = e + 1
                sub_graph.append([node1, node2, w])
                self.apply_union(parent, rank, search_node1, search_node2)
        
        cost = 0; new_Graph = []
        for N_1, N_2, weight in sub_graph:
            cost+=weight
            Graph_item = "{}--->{} = {}".format(str(N_1),str(N_2),str(weight))
            new_Graph.append(Graph_item)

        QMessageBox.about(self," Kruskal’s Algorithm result"," Minimum Spanning Tree (MST) is:{} {} {}Minimum Cost Spanning Tree is : {}".format("\n","\n".join(new_Graph),"\n",cost))
        
           
           

    # find array number and size it
    def find_arr_size(self):
        self.arr_number = [int(i) for i in self.Arr_area.toPlainText().split(",")]
        self.size_arr = len(self.arr_number)

    # close app if user clicked yes button
    def Q_exit(self):
        ask = QMessageBox.question(self,"Exit program","<b>Are you sure to exit the program!!</b>")
        if ask == QMessageBox.Yes:
            App.quit()

     # Insertion sort function
    def Insertion_sort(self):
        self.find_arr_size()
        Size = self.size_arr
        arr = self.arr_number
        for i in range(1, Size):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
            arr[j + 1] = key
        Sorted_arr = [str(i) for i in arr]
        QMessageBox.about(self,"Insertion sort result","sorted array by Insertion sort Algorithm :{} {}".format("\n",",".join(Sorted_arr)))

   # selection sort function
    def Selection_sort(self):
        self.find_arr_size()
        Size = self.size_arr
        arr = self.arr_number
        for i in range(Size):
            min_idx = i
            for j in range(i+1, Size):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        Sorted_arr = [str(i) for i in arr]
        QMessageBox.about(self,"Selection Sort result","sorted array by Selection sort Algorithm :{} {}".format("\n",",".join(Sorted_arr)))
    
    # binary search function
    def B_search(self):
        self.find_arr_size()
        arr = self.arr_number;arr.sort(); high = (self.size_arr) -1
        low = 0 ; key = self.item
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] == key :
                return QMessageBox.about(self,"Binary search result","<b>index of {} in array number after sorting is {}<\b>".format(key,mid+1))
            elif arr[mid] < key:low = mid + 1
            else:high = mid - 1
        return QMessageBox.about(self,"Binary search result"," <b>number you wont to search it not exist<\b>")
    
 
# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = MainWindow()


# start the app
sys.exit(App.exec_())
