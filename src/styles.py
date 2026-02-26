from tkinter import ttk
from tkinter import font

BACKGROUND_COLOR = "#1a1a1a"  # Very dark gray (almost black)
FOREGROUND_COLOR = "#e8e8e8"  # Light gray text
FIELD_COLOR = "#2d2d2d"  # Slightly lighter dark gray for fields
BORDER_COLOR = "#4a4a4a"  # Medium gray for borders
UNUSED_BACKGROUND_COLOR = "gray34"
BUTTON_COLOR = "#2d2d2d"  # Dark button background
BUTTON_HOVER_COLOR = "#3d3d3d"  # Slightly lighter on hover

def getDefaultFont(root=None):
    return font.Font(
        root=root,
        family="Segoe UI",  # More modern font
        size=11,
        weight="normal"
    )

def getTitleFont(root=None):
    return font.Font(
        root=root,
        family="Segoe UI",
        size=10,
        weight="normal"
    )

def initStyle(root):
    style = ttk.Style()
    style.theme_use("clam")
    
    # Global defaults
    style.configure(
        ".",
        background=BACKGROUND_COLOR,
        foreground=FOREGROUND_COLOR,
        font=getDefaultFont(root),
        fieldbackground=FIELD_COLOR
    )
    
    style.configure(
        "Unused_Window",
        background=UNUSED_BACKGROUND_COLOR,
        foreground=FOREGROUND_COLOR,
        font=getDefaultFont(root)
    )
    
    # Configure Text widget defaults (for multi-line text areas)
    root.option_add("*Text.background", FIELD_COLOR)
    root.option_add("*Text.foreground", FOREGROUND_COLOR)
    root.option_add("*Text.insertBackground", FOREGROUND_COLOR)  # Cursor color
    root.option_add("*Text.selectBackground", BORDER_COLOR)
    root.option_add("*Text.selectForeground", FOREGROUND_COLOR)
    root.option_add("*Text.highlightBackground", FIELD_COLOR)
    root.option_add("*Text.highlightColor", BORDER_COLOR)
    root.option_add("*Text.borderWidth", 1)
    root.option_add("*Text.relief", "solid")
    root.option_add("*Text.highlightThickness", 1)
    root.option_add("*Text.font", "Segoe\ UI 11")
    
    # Entry styling - rounded appearance with border
    style.configure(
        "TEntry",
        foreground=FOREGROUND_COLOR,
        fieldbackground=FIELD_COLOR,
        bordercolor=BORDER_COLOR,
        lightcolor=BORDER_COLOR,
        darkcolor=BORDER_COLOR,
        borderwidth=1,
        relief="solid",
        padding=(15, 12),  # Left/right, top/bottom padding for rounded look
        insertcolor=FOREGROUND_COLOR
    )
    
    style.map(
        "TEntry",
        bordercolor=[
            ("focus", BORDER_COLOR),
            ("!focus", BORDER_COLOR)
        ],
        lightcolor=[
            ("focus", BORDER_COLOR),
            ("!focus", BORDER_COLOR)
        ],
        darkcolor=[
            ("focus", BORDER_COLOR),
            ("!focus", BORDER_COLOR)
        ],
        fieldbackground=[
            ("focus", FIELD_COLOR),
            ("!focus", FIELD_COLOR)
        ]
    )
    
    # Label styling
    style.configure(
        "TLabel",
        background=BACKGROUND_COLOR,
        foreground=FOREGROUND_COLOR,
        font=getTitleFont(root)
    )
    
    # Button styling - dark with rounded appearance
    style.configure(
        "TButton",
        background=BUTTON_COLOR,
        foreground=FOREGROUND_COLOR,
        bordercolor=BORDER_COLOR,
        lightcolor=BORDER_COLOR,
        darkcolor=BORDER_COLOR,
        borderwidth=1,
        relief="solid",
        padding=(20, 15),
        font=getDefaultFont(root)
    )
    
    style.map(
        "TButton",
        background=[
            ("active", BUTTON_HOVER_COLOR),
            ("pressed", BUTTON_HOVER_COLOR)
        ],
        bordercolor=[
            ("focus", BORDER_COLOR),
            ("!focus", BORDER_COLOR)
        ]
    )
    
    # Frame styling
    style.configure(
        "TFrame",
        background=BACKGROUND_COLOR
    )
    
    # Scrollbar styling
    style.configure(
        "Vertical.TScrollbar",
        background=FIELD_COLOR,
        troughcolor=FIELD_COLOR,
        bordercolor=BORDER_COLOR,
        arrowcolor=FOREGROUND_COLOR,
        relief="solid",
        borderwidth=1
    )
    
    style.map(
        "Vertical.TScrollbar",
        background=[
            ("active", BORDER_COLOR),
            ("pressed", BORDER_COLOR),
            ("!active", FIELD_COLOR)
        ]
    )
    
    style.configure(
        "Invisible.Vertical.TScrollbar",
        gripcount=0,
        background=BACKGROUND_COLOR,
        darkcolor=BACKGROUND_COLOR,
        lightcolor=BACKGROUND_COLOR,
        troughcolor=BACKGROUND_COLOR,
        bordercolor=BACKGROUND_COLOR,
        arrowcolor=BACKGROUND_COLOR,
        relief="flat",
        borderwidth=0
    )
    
    style.layout("Invisible.Vertical.TScrollbar", [
        ("Vertical.Scrollbar.trough", {
            "children": [
                ("Vertical.Scrollbar.thumb", {
                    "expand": "1",
                    "sticky": "nswe"
                })
            ],
            "sticky": "ns"
        })
    ])
    
    # Combobox styling
    style.configure(
        "TCombobox",
        fieldbackground=FIELD_COLOR,
        background=FIELD_COLOR,
        foreground=FOREGROUND_COLOR,
        bordercolor=BORDER_COLOR,
        lightcolor=BORDER_COLOR,
        darkcolor=BORDER_COLOR,
        arrowcolor=FOREGROUND_COLOR,
        relief="solid",
        borderwidth=1,
        padding=(15, 12),
        insertcolor=FOREGROUND_COLOR
    )
    
    style.layout("TCombobox", [
        ('Combobox.field', {
            'children': [(
                'Combobox.downarrow', {
                    'side': 'right',
                    'sticky': 'ns'
                }
            ), (
                'Combobox.padding', {
                    'children': [(
                        'Combobox.textarea', {
                            'sticky': 'nswe'
                        }
                    )],
                    'expand': '1',
                    'sticky': 'nswe'
                }
            )],
            'sticky': 'nswe'
        })
    ])
    
    style.map(
        "TCombobox",
        fieldbackground=[
            ("readonly", FIELD_COLOR),
            ("disabled", FIELD_COLOR)
        ],
        foreground=[
            ("readonly", FOREGROUND_COLOR),
            ("disabled", FOREGROUND_COLOR)
        ],
        background=[
            ("readonly", FIELD_COLOR),
            ("disabled", FIELD_COLOR)
        ],
        bordercolor=[
            ("focus", BORDER_COLOR),
            ("readonly", BORDER_COLOR)
        ]
    )

    #spinbox
    style.configure(
        "TSpinbox",
        fieldbackground=FIELD_COLOR,
        background=FIELD_COLOR,
        foreground=FOREGROUND_COLOR,
        bordercolor=BORDER_COLOR,
        lightcolor=BORDER_COLOR,
        darkcolor=BORDER_COLOR,
        arrowcolor=FOREGROUND_COLOR,
        relief="solid",
        borderwidth=1,
        padding=(15, 12),
        insertcolor=FOREGROUND_COLOR
    )

    style.map(
        "TSpinbox",
        fieldbackground=[("readonly", FIELD_COLOR)],
        foreground=[("readonly", FOREGROUND_COLOR)],
        background=[("readonly", FIELD_COLOR)],
        bordercolor=[
            ("focus", BORDER_COLOR),
            ("!focus", BORDER_COLOR)
        ]
    )
    
    # Option add for better control
    root.option_add("*TCombobox*Listbox*selectBackground", FIELD_COLOR)
    root.option_add("*TCombobox*Listbox*selectForeground", FOREGROUND_COLOR)
    root.option_add("*TCombobox*Entry*selectBackground", FIELD_COLOR)
    root.option_add("*TCombobox*Entry*selectForeground", FOREGROUND_COLOR)
    root.option_add("*TCombobox*highlightBackground", FIELD_COLOR)
    root.option_add("*TCombobox*highlightColor", FIELD_COLOR)
    root.option_add("*TCombobox*background", FIELD_COLOR)
    root.option_add("*TCombobox*Entry*background", FIELD_COLOR)

    style.configure("TESTING.TFrame", background="red")
    
    return style

def getCalendarStyle():
    return {
        "background": FIELD_COLOR,
        "foreground": FOREGROUND_COLOR,
        "bordercolor": BORDER_COLOR,
        "headersbackground": FIELD_COLOR,
        "headersforeground": FOREGROUND_COLOR,
        "normalbackground": BACKGROUND_COLOR,
        "normalforeground": FOREGROUND_COLOR,
        "weekendbackground": BACKGROUND_COLOR,
        "weekendforeground": FOREGROUND_COLOR,
        "selectbackground": BORDER_COLOR,
        "selectforeground": FOREGROUND_COLOR,
        "othermonthbackground": BACKGROUND_COLOR,
        "othermonthforeground": BORDER_COLOR,
        "othermonthwebackground": BACKGROUND_COLOR,
        "othermonthweforeground": BORDER_COLOR,
        "todaybackground": FIELD_COLOR,
        "todayforeground": FOREGROUND_COLOR,
    }

