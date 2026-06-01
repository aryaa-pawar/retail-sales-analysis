from PIL import Image

# Load images
img1 = Image.open("image/revenuebycategory.png")
img2 = Image.open("image/top10.png")
img3 = Image.open("image/regional.png")
img4 = Image.open("image/profitanalysis.png")

# Resize all to same size
width = 800
height = 500

img1 = img1.resize((width, height))
img2 = img2.resize((width, height))
img3 = img3.resize((width, height))
img4 = img4.resize((width, height))

# Create canvas
dashboard = Image.new(
    "RGB",
    (width * 2, height * 2),
    color="white"
)

# Paste images
dashboard.paste(img1, (0, 0))
dashboard.paste(img2, (width, 0))
dashboard.paste(img3, (0, height))
dashboard.paste(img4, (width, height))

# Save
dashboard.save("image/dashboard_summary.png")

print("Dashboard created!")