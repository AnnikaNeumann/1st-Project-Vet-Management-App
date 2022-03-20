from flask import Flask, render_template, redirect, request, Blueprint
from modules.animal import Animal
from modules.owner import Owner
from repositories.owner_repo import select_last_name
from repositories import animal_repo
from repositories import owner_repo
from repositories import vet_repo

vet_blueprint = Blueprint("animal", __name__)


@vet_blueprint.route("/new_client", methods =['GET'])
def new_client():

    return render_template("/new.html")


@vet_blueprint.route("/new_client/save_new_client", methods=['POST'])
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


@vet_blueprint.route("/search/<owner_id>", methods =['GET'])
def display_client(owner_id):

    owner = owner_repo.select_by_id(owner_id)
    animals = animal_repo.select_animal_by_owner_id(owner.id)

    return render_template("/view_client.html",owner = owner,animals = animals)


@vet_blueprint.route("/search/search_action", methods =['POST'])
def search_for_client():

    last_name = request.form["last_name"]
    owners = owner_repo.select_last_name(last_name)

    # animal = animal_repo.select_animal(owner_id)

    return render_template('/view_clients.html',owners=owners)

    


