from linpgtoolbox.builder import Builder

# compile all files
additional_files: tuple[str, ...] = ("README.md", "LICENSE")
Builder.compile(
    "linpgassets",
    additional_files=additional_files,
    update_the_one_in_sitepackages=True,
    include_pyinstaller_program=True,
)

# prompt compile is done
for i in range(2):
    print("")
print("--------------------Done!--------------------")
for i in range(2):
    print("")

# upload the latest build
"""
match input("Do you want to package and upload the latest build (Y/n):"):
    case "Y":
        Builder.build()
        Builder.upload()
    case "N":
        Builder.remove("src")
"""
