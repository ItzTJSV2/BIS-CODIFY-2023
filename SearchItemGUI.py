import tkinter as tk
from tkinter import ttk
from ttkbootstrap.constants import *
from addnsearch import *


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Lost and Found')
        self.style = ttk.Style()
        self.geometry("600x750")
        self.resizable(False, False)

        mf = MainFrame(self)
        mf.pack(fill="both")


class MainFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cumulativeRow = 0

        # Type tags
        self.typs = [
            "Bottle",
            "Backpack",
            "Uniforms/Shirts",
            "Uniforms/Belts", "Uniforms/Pants",
            "Uniforms/Hoodies",
            "Stationaries/Pencil case",
            "Stationaries/Calculators",
            "Valuables/Phones",
            "Valuables/Laptops",
            "Valuables/Watches"
        ]

        # Colour tags
        self.clrs = [
            "Black",
            "Gray",
            "White",
            "Navy",
            "Yellow",
            "Green",
            "Red",
            "Blue",
            "Orange"
        ]

        # Location tags
        self.locs = [
            "Gym",
            "Field",
            "1st building",
            "2nd building",
            "3rd building",
            "Boy's bathroom",
            "Girl's bathroom",
            "Girl's changing room",
            "Boy's changing room"
        ]

        self.typsChosen = []
        self.clrsChosen = []
        self.locsChosen = []

        self.df = CollapsingFrame(self)
        self.sf = CollapsingFrame(self)

        tglBtn = ttk.Button(
            master=self,
            text="test",
            command=lambda c=(self.sf, self.df): self.toggleTab(c[0], c[1])
        )
        tglBtn.grid(row=0, column=0, sticky='ew')
        self.sf.grid(row=1, column=0, sticky='news')

        self.cumulativeRow += 2
        # self.add(self.sf, self.df)

        # search
        self.search()

        self.display([], [], [])

    def toggleTab(self, sf, df):
        if sf.winfo_viewable():
            sf.grid_remove()
            df.grid()
        else:
            df.grid_remove()
            sf.grid()

    def search(self):
        self.sf.separator()

        # search - Type
        typTag = ttk.Frame(self.sf, padding=10)
        for i, name in enumerate(self.typs, 0):
            self.typsChosen.append(tk.BooleanVar(value=False))
            option = ttk.Checkbutton(
                master=typTag,
                bootstyle="toolbutton",
                cursor="hand",
                text=name,
                variable=self.typsChosen[i]
            )
            option.grid(column=i % 5, row=i // 5)
        self.sf.add(typTag, title="Types")

        self.sf.separator()

        # search - Colour
        clrTag = ttk.Frame(self.sf, padding=10)
        for i, name in enumerate(self.clrs, 0):
            self.clrsChosen.append(tk.BooleanVar(value=False))
            option = ttk.Checkbutton(
                master=clrTag,
                bootstyle="toolbutton",
                cursor="hand",
                text=name,
                variable=self.clrsChosen[i]
            )
            option.grid(column=i % 5, row=i // 5)
        self.sf.add(clrTag, title="Colours")

        self.sf.separator()

        # search - Location
        locTag = ttk.Frame(self.sf, padding=10)
        for i, name in enumerate(self.locs, 0):
            self.locsChosen.append(tk.BooleanVar(value=False))
            option = ttk.Checkbutton(
                master=locTag,
                bootstyle="toolbutton",
                cursor="hand",
                text=name,
                variable=self.locsChosen[i]
            )
            option.grid(column=i % 5, row=i // 5)
        self.sf.add(locTag, title="Locations")

        self.sf.separator()

    def display(self, types: list, colours: list, locations: list):
        """
        Table format
            ItemID INTEGER PRIMARY KEY,
            ItemName TEXT NOT NULL,
            Location TEXT NOT NULL,
            DirecImage TEXT NOT NULL,
            DateFound DATE NOT NULL,
            Colour INTEGER NOT NULL,
            Type INTEGER NOT NULL,
            Found INTEGER DEFAULT 0,
            Security INTEGER DEFAULT 0,
            FreeToAll INTEGER DEFAULT 0
        """
        self.example = [
            [17, 'bottle', 0, 'image.png', '2023-03-01', '-2-3-', 0, 0, 0, 0],
            [19, 'bag', 3, 'image2.png', '2023-02-27', '-0-4-', 1, 0, 0, 0]
        ]
        # Format: [[item1], [item2]]
        # items = searchItem(types, colours, locations)
        items = self.example

        displayer = ttk.Frame(self.df, padding=10)
        for i, item in enumerate(items, 0):
            itemProfile = ttk.Frame(displayer, padding=10)
            itemProfile.grid(row=i, column=0, sticky='ew')
            img = ttk.Label(
                master=itemProfile,
                text=item[3],
                # height=20,
                # width=20,
                padding=5
            )
            img.grid(row=0, column=0, rowspan=2)
            title = ttk.Label(
                master=itemProfile,
                text=item[1],
                # height=10,
                # width=30
            )
            title.grid(row=0, column=1, padx=5, pady=0)
            tags = ttk.Label(
                master=itemProfile,
                text=item[5],
                # height=10
            )
            tags.grid(row=1, column=1, padx=5, pady=0)
        self.df.add(displayer, title="Items")


class CollapsingFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cumulativeRow = 0

    def add(self, child, title=""):
        tab = ttk.Frame(self)
        tab.grid(row=self.cumulativeRow, column=0, sticky='ew')

        title = ttk.Label(master=tab, text=title)
        title.pack(side=LEFT, fill=BOTH, padx=20)

        tglBtn = ttk.Button(
            master=tab,
            text="test",
            command=lambda c=child: self.toggleTab(c)
        )
        tglBtn.pack(side='left')

        child.tglBtn = tglBtn
        child.grid(row=self.cumulativeRow + 1, column=0, sticky='news')

        self.cumulativeRow += 2

    def separator(self):
        sep = ttk.Separator(
            master=self,
            bootstyle="primary"
        )
        sep.grid(row=self.cumulativeRow, column=0, sticky='ew', pady=5)

        self.cumulativeRow += 1

    def toggleTab(self, child):
        if child.winfo_viewable():
            child.grid_remove()
        else:
            child.grid()


if __name__ == '__main__':
    Application().mainloop()
