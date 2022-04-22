import json


LANGUAGE = "python"
META_FILE = "project_meta.json"
PROJECT_PAGE_TEMPLATE = "project_page_template.html"


categories = {
    "Data Structures & Algorithm": {
        "html": f"{LANGUAGE}_projects_dsa.html",
        "projects": [],
    },
    "Desktop Application": {
        "html": f"{LANGUAGE}_projects_desktop_application.html",
        "projects": [],
    },
    "Game Development": {
        "html": f"{LANGUAGE}_projects_game_development.html",
        "projects": [],
    },
    "Scripting & Automation": {
        "html": f"{LANGUAGE}_projects_scripting_and_automation.html",
        "projects": [],
    },
    "Web Development": {
        "html": f"{LANGUAGE}_projects_web_development.html",
        "projects": [],
    },
}


# load meta file
with open(META_FILE, "r") as file:
    projects = json.load(file)


# transfer meta file to categories
for project in projects:
    project_title = project["title"]
    for category in project["categories"]:
        if category not in categories:
            print(f"[X] {project_title} category {category} not registered")
            continue
        categories[category]["projects"].append(project)


# process by category
for category, details in categories.items():
    projects = sorted(details["projects"], key=lambda x: x["importance"], reverse=True)
    articles = ""
    scripts = ""

    for project in projects:
        title = project["title"]
        filename = project["filename"]
        if project["technologies"]:
            technologies = " | ".join(project["technologies"])
        else:
            technologies = "None/Minor Libraries Involved"
        description = project["description"]
        privacy = project["privacy"]
        github = project["github"]
        has_gif = project["gif"]

        if privacy == "public":
            reference = f"""<a href="{github}" class="special">View Source Code</a>"""
        elif privacy == "private":
            reference = f"""<a href="#" class="special2" style="color: rgba(125, 125, 125, 1);">Private Source Code</a>"""
        elif privacy == "client":
            reference = f"""<a href="#" class="special2" style="color: rgba(125, 125, 125, 1);">Confidential Source Code</a>"""
        else:
            reference = ""
            print(f"[X] Invalid privacy for project: {title}")

        articles += f"""                                    <article>
										<a class="image"><img src="../../images/{filename}.png" id="{filename}" alt="" /></a>
										<h3 class="major">{title}</h3>
										<p>{technologies}<br><br>{description}</p>
										{reference}
									</article>\n"""

        if not has_gif:
            continue

        scripts += f"""
				$(function() {{
						$("#{filename}").hover(
							function() {{
								$(this).attr("src", "../../images/{filename}.gif");
							}},
							function() {{
								$(this).attr("src", "../../images/{filename}.png");
							}}
						);
					}});"""

    with open(PROJECT_PAGE_TEMPLATE, "r") as file:
        html = file.read()

    html = html.replace("{% category %}", category)
    html = html.replace("{% articles %}", articles)
    html = html.replace("{% scripts %}", scripts)

    with open(details["html"], "w") as file:
        file.write(html)

