from flask import Flask, render_template, redirect, request

from flask import Blueprint
from project.modules.animal import Animal
from repositories import animal_repo
from repositories import owner_repo
from repositories import vet_repo
from modules.owner import Owner

vet_blueprint = Blueprint("animal", __name__)

@vet_blueprint.route("/add", methods =['POST'])
def new_animal():
    name = request.form["name"]
    dob = request.form["dob"]
    breed = request.form ["breed"]
    treatments = request.form ["treatments"]
    
    animal = animal_repo.select(id)
    animal = Animal(name, dob, breed, treatments)
    

    animal_repo.save(animal)
    return redirect('/animal')



@vet_blueprint.route("search")
def search_animal():
    animal = animal_repo.select_all()
    owner = owner_repo.select_all()
    return render_template('/search', all_animal = animal)

@vet_blueprint.route
