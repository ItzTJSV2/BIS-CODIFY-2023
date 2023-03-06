# Construct GUI
import tkinter as tk
import ttkbootstrap as ttk

# Fetch image
from PIL import Image
import customtkinter

# fetch data from database
from addnSearch import *


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Lost and Found')
        self.style = ttk.Style()
        self.geometry("700x800")
        self.resizable(False, False)

        mf = MainFrame(self)
        mf.pack(fill="both", pady=40)


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

        # Controls different options chosen from the 'search' tab
        self.typsChosen = []
        self.clrsChosen = []
        self.locsChosen = []
        self.typsPassed = []
        self.clrsPassed = []
        self.locsPassed = []

        self.displayNav = ttk.Frame(self)
        self.searchNav = ttk.Frame(self)
        self.sf = ttk.Frame(self, padding=20)
        self.df = ttk.Frame(self, padding=20)

        self.displayNav.grid(row=0, column=0, sticky='w')
        self.searchNav.grid(row=1, column=0, sticky='w')
        self.sf.grid(row=2, column=0)
        self.df.grid(row=3, column=0)

        self.displayNavigation(self.displayNav)
        self.searchNavigation(self.searchNav)
        self.search(self.sf)
        self.display([], [], [])
        self.toggleTab()

    def displayNavigation(self, frame):
        # Construct a button that opens 'search' tab, closing 'display' tab
        tglBtn = ttk.Button(
            master=frame,
            text="🔎 SEARCH",
            bootstyle='dark-outline',
            command=lambda: self.toggleTab()
        )
        tglBtn.grid(row=0, column=0, padx=20, sticky='w')

    def searchNavigation(self, frame):
        # Construct a button that refreshes the 'display' tab using 'chosen tags' + open it
        tglBtn = ttk.Button(
            master=frame,
            text="ENTER ⮐",
            bootstyle='dark-outline',
            command=lambda: self.refresh()
        )
        tglBtn.grid(row=0, column=0, padx=20, sticky='w')

        # Construct a button that restores the 'chosen tag' valye to before moving to 'search' + open 'display' tab
        tglBtn = ttk.Button(
            master=frame,
            text="CANCEL",
            bootstyle='dark-outline',
            command=lambda: self.cancel()
        )
        tglBtn.grid(row=0, column=1, padx=20, sticky='e')

    def search(self, frame):
        containerInfo = [
            (0, "TYPES", self.typs, self.typsChosen),
            (1, "COLOURS", self.clrs, self.clrsChosen),
            (2, "LOCATIONS", self.locs, self.locsChosen),
        ]

        # Iterate, construct three containers with checkboxes in it
        for info in containerInfo:
            container = ttk.Labelframe(frame, padding=10, text=info[1], bootstyle='dark')
            container.grid(column=0, row=info[0], pady=10)
            for i, name in enumerate(info[2], 0):
                # Set up the 'Chosen tag' list. (Can't be done at line 71-76 because 'tk.BooleanVar's must all have different id)
                info[3].append(tk.BooleanVar(value=False))

                # Construct a frame to fix width & height of checkbutton
                frm = ttk.Frame(master=container, width=150, height=25)
                frm.grid(column=i % 4, row=i // 4, padx=0, pady=3)
                frm.pack_propagate(0)

                # Construct the checkbutton
                option = ttk.Checkbutton(
                    master=frm,
                    bootstyle='success-round-toggle',
                    text=name,
                    variable=info[3][i]
                )
                option.pack(side='left')

    def display(self, types: list, colours: list, locations: list, code=0):
        """
        Table format
            ItemID INTEGER PRIMARY KEY,
            ItemName TEXT NOT NULL,
            Location INTEGER NOT NULL,
            DirecImage TEXT NOT NULL,
            DateFound DATE NOT NULL,
            Colour TEXT NOT NULL,
            Type INTEGER NOT NULL,
            Found INTEGER DEFAULT 0,
            Security INTEGER DEFAULT 0,
            FreeToAll INTEGER DEFAULT 0
        """

        # Format: [[item1], [item2]]
        items = searchItem(types, colours, locations)
        """
        # Sample data
        items = [[1, 'bottle1', 3, 'images/apple.jpg', '2023-02-28', '-2-4-7-8-', 2, 0, 0, 0],
                 [2, 'bottle1', 1, 'images/apple.jpg', '2023-02-28', '-0-1-', 4, 0, 0, 0],
                 [3, 'bottle1', 4, 'images/apple.jpg', '2023-02-28', '-3-5-6-', 1, 0, 0, 0],]
        
        if code == 1:
            items = [[1, 'dfa', 3, 'images/apple.jpg', '2023-02-28', '-2-4-7-8-', 2, 0, 0, 0],
                    [2, 'ghgh', 1, 'images/apple.jpg', '2023-02-28', '-3-2-', 1, 0, 0, 0],]
        """


        # Iterate, Construct containers with detail of each item in it
        for i, item in enumerate(items, 0):
            itemProfile = ttk.Labelframe(
                self.df, padding=10, text=i + 1, bootstyle='dark')
            itemProfile.grid(row=i, column=0, padx=0, pady=10)

            # Insert an image
            imgLabel = customtkinter.CTkLabel(
                itemProfile, width=15, height=15, text="")
            imgLabel.grid(row=0, column=0, rowspan=2)
            img = customtkinter.CTkImage(
                light_image=Image.open(item[3]), size=(90, 90))
            imgLabel.configure(image=img)

            # Insert a title
            title = ttk.Label(
                master=itemProfile,
                text=item[1].upper(),
                bootstyle='success',
                font=("Noto sans", 25, 'bold'),
                width=30
            )
            title.grid(row=0, column=1, columnspan=3, padx=7, pady=0)

            if len(item[5]) >= 7:
                item[5] = item[5][:7]
            # 0: Types, 1: Colours, 2: Locations
            tagsInfo = [
                (1, self.getTags(self.typs, str(item[6]))),
                (2, self.getTags(self.clrs, item[5][1:-1])),
                (3, self.getTags(self.locs, str(item[2])))
            ]

            # Iterate, construct labels that has detail of the item
            for info in tagsInfo:
                tag = ttk.Label(
                    master=itemProfile,
                    text=info[1],
                    bootstyle='secondary',
                    font=('Noto sans', 12, 'italic')
                )
                tag.grid(row=1, column=info[0], padx=0, pady=0, sticky='w')

    def getTags(self, source, index: str):
        # Reform str(id) --> str(name): "-7-5-" --> "# Black  # Yellow"
        tags = ""
        index = index.split("-")
        for i in index:
            tags += "# " + source[int(i)] + "  "
        return tags

    def toggleTab(self):
        # Switch between 'search' tab and 'display' tab
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

    def refresh(self):
        updates = [
            [self.typsPassed, self.typsChosen],
            [self.clrsPassed, self.clrsChosen],
            [self.locsPassed, self.locsChosen]
        ]

        # Iterate, update 'chosen tag -- passed' list
        for [target, criteria] in updates:
            for i in range(len(criteria)):
                if criteria[i].get() == True:
                    target.append(i)
        
        # Update 'display' tab by writing over the existing frame
        self.display(self.typsPassed, self.clrsPassed, self.locsPassed, 1)

        # Switch the display
        self.toggleTab()

    def cancel(self):
        updates = [
            [self.typsChosen, self.typsPassed],
            [self.clrsChosen, self.clrsPassed],
            [self.locsChosen, self.locsPassed]
        ]

        # Iterate, restore the 'chosen tag' list of previous search (In case user doesn't like the change that he made)
        for [target, criteria] in updates:
            for i in range(len(target)):
                if i in criteria:
                    target[i].set(True)
                else:
                    target[i].set(False)

        # Switch the display
        self.toggleTab()


if __name__ == '__main__':
    Application().mainloop()
