from flask import Flask, render_template, redirect, request

from flask import Blueprint
from repositories import animal_repo
from repositories import owner_repo
from repositories import vet_repo

vet_blueprint = Blueprint("animal", __name__)

@vet_blueprint.route("/add", methods =['POST'])
def new_animal():
    name = request.form["name"]
    dob = request.form["dob"]
    breed = request.form ["breed"]
    treatments = request.form ["treatments"]

    animal = animal_repo.select(id)
    animal = Animal(name, dob, breed, treatments, owner_id)
    

    animal_repo.save(animal)
    return redirect('/animal')



@vet_blueprint.route("/search", methods =["GET"])
def search_animal():
    return render_template("/search.html", all_animal = animals)

