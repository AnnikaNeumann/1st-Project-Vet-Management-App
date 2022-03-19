from flask import Flask, render_template, redirect, request, Blueprint
from modules.animal import Animal
from modules.owner import Owner
from repositories import animal_repo
from repositories import owner_repo
from repositories import vet_repo

vet_blueprint = Blueprint("animal", __name__)


@vet_blueprint.route("/new_client", methods =['GET'])
def new_client():

    return render_template("/new.html")


@vet_blueprint.route("/save_new_client", methods=['POST'])
def save_new_client():

    name = request.form["name"]
    dob = request.form["DOB"]
    breed = request.form["breed"]
    treatments = request.form["treatments"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    number = request.form ["number"]

    owner = Owner(first_name, last_name, number)
    animal = Animal(name, dob, breed, treatments)
    
    saved_owner = owner_repo.save(owner)
    animal.owner_id = saved_owner.id
    animal_repo.save(animal)

    return redirect('/submit')

    # return render_template("/new.html")

@vet_blueprint.route("/submit", methods =['GET'])
def submit():
    return render_template("/submit.html")



@vet_blueprint.route("/search", methods =['GET'])
def search_here():

    return render_template("/search.html")


@vet_blueprint.route("/search_for_client", methods =['POST'])
def search_for_client():

    last_name = request.form["last_name"]

    return redirect('/submit')

    


