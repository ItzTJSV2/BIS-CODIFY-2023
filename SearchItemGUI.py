import tkinter as tk
import ttkbootstrap as ttk
from addnsearch import *


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Lost and Found')
        self.style = ttk.Style()
        self.geometry("700x800")
        self.resizable(False, False)

        # self.s = ttk.Style()
        # self.s.configure(
        #     'TCheckbutton',
        #     background='white',
        #     font=('Helvetica', 12, 'bold')
        # )
        # self.s.map('TCheckbutton',
        #            foreground=[('disabled', 'yellow'),
        #                        ('pressed', 'red'),
        #                        ('active', 'blue')],
        #            background=[('disabled', 'magenta'),
        #                        ('pressed', 'cyan'),
        #                        ('active', 'green')])

        mf = MainFrame(self)
        mf.pack(fill="both")


class MainFrame(ttk.Labelframe):
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

        self.displayNav = ttk.Frame(self, bootstyle="info")
        self.searchNav = ttk.Frame(self, bootstyle="info")
        self.sf = ttk.Labelframe(self, padding=20)
        self.df = ttk.Labelframe(self, padding=20)

        self.displayNav.grid(row=0, column=0)
        self.searchNav.grid(row=1, column=0)
        self.sf.grid(row=2, column=0)
        self.df.grid(row=3, column=0)

        self.displayNavigation(self.displayNav)
        self.searchNavigation(self.searchNav)
        self.search(self.sf)
        self.display([], [], [])
        self.toggleTab()

    def toggleTab(self):
        if self.df.winfo_viewable():
            self.displayNav.grid_remove()
            self.df.grid_remove()
            self.searchNav.grid()
            self.sf.grid()
        else:
            self.sf.grid_remove()
            self.searchNav.grid_remove()
            self.displayNav.grid()
            self.df.grid()

    def displayNavigation(self, frame):
        tglBtn = ttk.Button(
            master=frame,
            text="🔎Search",
            command=lambda: self.toggleTab()
        )
        tglBtn.grid(row=0, column=0)

    def searchNavigation(self, frame):
        tglBtn = ttk.Button(
            master=frame,
            text="enter",
            command=lambda: self.toggleTab()
        )
        tglBtn.grid(row=0, column=0)

    def search(self, frame):
        # search - Type
        typTag = ttk.Labelframe(frame, padding=10,
                                text='types', bootstyle='primary')
        typTag.grid(column=0, row=0, pady=5)
        for i, name in enumerate(self.typs, 0):
            self.typsChosen.append(tk.BooleanVar(value=False))
            frm = ttk.Frame(master=typTag, width=150, height=25)
            frm.grid(column=i % 4, row=i // 4, padx=0, pady=3)
            frm.pack_propagate(0)
            option = ttk.Checkbutton(
                master=frm,
                cursor="hand",
                bootstyle='success-round-toggle',
                text=name,
                variable=self.typsChosen[i]
            )
            option.pack(side='left')

        # search - Colour
        clrTag = ttk.Labelframe(frame, padding=10,
                                text='Colours', bootstyle='primary')
        clrTag.grid(column=0, row=1, pady=5)
        for i, name in enumerate(self.clrs, 0):
            self.clrsChosen.append(tk.BooleanVar(value=False))
            frm = ttk.Frame(master=clrTag, width=150, height=25)
            frm.grid(column=i % 4, row=i // 4, padx=0, pady=3)
            frm.pack_propagate(0)
            option = ttk.Checkbutton(
                master=frm,
                cursor="hand",
                bootstyle='success-round-toggle',
                text=name,
                variable=self.clrsChosen[i]
            )
            option.pack(side='left')

        # search - Location
        locTag = ttk.Labelframe(frame, padding=10,
                                text='Locations', bootstyle='primary')
        locTag.grid(column=0, row=2, pady=5)
        for i, name in enumerate(self.locs, 0):
            self.locsChosen.append(tk.BooleanVar(value=False))
            frm = ttk.Frame(master=locTag, width=150, height=25)
            frm.grid(column=i % 4, row=i // 4, padx=0, pady=3)
            frm.pack_propagate(0)
            option = ttk.Checkbutton(
                master=frm,
                cursor="hand",
                bootstyle='success-round-toggle',
                text=name,
                variable=self.locsChosen[i]
            )
            option.pack(side='left')

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
            [19, 'bag', 3, 'image.png', '2023-02-27', '-0-4-', 1, 0, 0, 0]
        ]
        # Format: [[item1], [item2]]
        # items = searchItem(types, colours, locations)
        items = self.example

        for i, item in enumerate(items, 0):
            itemProfile = ttk.Labelframe(self.df, padding=10)
            itemProfile.grid(row=i, column=0, padx=0, pady=3)
            itemProfile.pack_propagate(0)
            """
            ImageLabel = customtkinter.CTkLabel(ImageInputFrame, width=300, height=300, text="")
            ImageLabel.grid(row=0, column=1, rowspan=3)
            """
            imgLabel = ttk.Label(
                master=itemProfile,
                text=item[3],
                width=15,
                bootstyle='inverse-success',
                padding=5
            )
            imgLabel.grid(row=0, column=0, rowspan=2)
            imgLabel.pack_propagate(0)
            title = ttk.Label(
                master=itemProfile,
                text=item[1],
                bootstyle='inverse-info',
                width=30
            )
            title.grid(row=0, column=1, padx=5, pady=0)
            title.pack_propagate(0)
            tags = ttk.Label(
                master=itemProfile,
                text=item[5],
                bootstyle='inverse-danger'
            )
            tags.grid(row=1, column=1, padx=5, pady=0)
            tags.pack_propagate(0)


class CollapsingFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cumulativeRow = 0

    def add(self, child, title=""):
        tab = ttk.Frame(self)
        tab.grid(row=self.cumulativeRow, column=0)

        title = ttk.Label(master=tab, text=title)
        title.pack(side='left', fill='both', padx=20)

        tglBtn = ttk.Button(
            master=tab,
            text="test",
            command=lambda c=child: self.toggleTab(c)
        )
        tglBtn.pack(side='left')

        child.tglBtn = tglBtn
        child.grid(row=self.cumulativeRow + 1, column=0)

        self.cumulativeRow += 2

    def toggleTab(self, child):
        if child.winfo_viewable():
            child.grid_remove()
        else:
            child.grid()


if __name__ == '__main__':
    Application().mainloop()
