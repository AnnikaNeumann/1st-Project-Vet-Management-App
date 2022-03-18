from flask import Flask, render_template, redirect, request

from flask import Blueprint
from repositories import animal_repo
from repositories import owner_repo
from repositories import vet_repo
from modules.owner import Owner

vet_blueprint = Blueprint("animal", __name__)

@vet_blueprint.route("/add")
def animal():
    animal = animal_repo.select_all()
    return render_template("animal/index.html", add_animal = animal)

    