import ast
import os
from flask import Blueprint, render_template
from flask_login import login_required

arch_bp = Blueprint("arch", __name__)

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LAYERS = [
    {
        "name": "Presentation Layer",
        "role": "HTTP routes, request handling, template rendering",
        "files": [
            "app/presentation/auth_routes.py",
            "app/presentation/request_routes.py",
            "app/presentation/volunteer_routes.py",
            "app/presentation/admin_routes.py",
        ],
    },
    {
        "name": "Application / Service Layer",
        "role": "Use cases, business rules, orchestration",
        "files": ["app/services/services.py"],
    },
    {
        "name": "Domain Layer",
        "role": "Core entities and relationships",
        "files": ["app/domain/models.py"],
    },
    {
        "name": "Data Access Layer",
        "role": "Repositories — persistence and queries",
        "files": ["app/data/repositories.py", "app/data/seed.py"],
    },
]

PATTERN_FILES = ["app/strategies/matching_strategy.py"]


def summarize(relpath):
    path = os.path.join(BASE, relpath)
    if not os.path.exists(path):
        return {"file": relpath, "classes": [], "functions": []}
    with open(path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    classes = []
    functions = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            methods = []
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    args = [a.arg for a in item.args.args if a.arg != "self"]
                    methods.append({"name": item.name, "args": args})
            bases = []
            for b in node.bases:
                if isinstance(b, ast.Name):
                    bases.append(b.id)
                elif isinstance(b, ast.Attribute):
                    bases.append(b.attr)
            classes.append({"name": node.name, "bases": bases, "methods": methods})
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = [a.arg for a in node.args.args]
            functions.append({"name": node.name, "args": args})
    return {"file": relpath, "classes": classes, "functions": functions}


@arch_bp.route("/architecture")
@login_required
def architecture():
    layers = []
    for layer in LAYERS:
        layers.append({
            "name": layer["name"],
            "role": layer["role"],
            "modules": [summarize(f) for f in layer["files"]],
        })
    pattern = [summarize(f) for f in PATTERN_FILES]
    return render_template("architecture.html", layers=layers, pattern=pattern)
