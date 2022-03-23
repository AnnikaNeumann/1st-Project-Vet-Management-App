from flask import Flask, render_template, redirect, request, Blueprint
from modules.animal import Animal
from modules.owner import Owner
from modules.vet import Vet

from repositories.owner_repo import select_last_name
from repositories.animal_repo import select_animal_by_owner

from repositories import animal_repo
from repositories import owner_repo
from repositories import vet_repo

vet_blueprint = Blueprint("animal", __name__)

@vet_blueprint.route("/all", methods =['GET'])
def view_all():

    owners = owner_repo.select_all()
    return render_template("/view_all.html", owners = owners)

# route to get to the front page /new_client to add a new animal
@vet_blueprint.route("/new_client", methods =['GET'])
def new_client():

    vets = vet_repo.select_all()
    return render_template("/new.html", vets = vets)

# route to save the client after inputting details to form
@vet_blueprint.route("/new_client/save_new_client", methods=['POST'])
def save_new_client():

    name = request.form["name"]
    dob = request.form["DOB"]
    species = request.form["species"]
    treatments = request.form["treatments"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    number = request.form ["number"]
    vet_id = request.form["vet_id"]

    vet = vet_repo.select_by_id(vet_id)    

    owner = Owner(first_name, last_name, number)
    animal = Animal(name, dob, species, treatments, owner, vet, id)
    animal.vet_id = vet_id
    saved_owner = owner_repo.save(owner)
    animal.owner_id = saved_owner.id
    animal_repo.save(animal)


    return redirect('/submit')

# route which functions when we click on submit when we save an animal
@vet_blueprint.route("/submit", methods =['GET'])
def submit():
    return render_template("/submit.html")

# route which functions when we click on search in the nav
@vet_blueprint.route("/search", methods =['GET'])
def search_here():
    return render_template("/search.html")

# route which functions when we click on the owner, which is being listed after the last funciton
@vet_blueprint.route("/search/<owner_id>", methods =['GET'])
def display_client(owner_id):

    owner = owner_repo.select_by_id(owner_id)
    animals = animal_repo.select_animal_by_owner(owner)
    return render_template("/view_client.html",owner = owner, animals = animals)


@vet_blueprint.route("/search/search_action", methods =['POST'])
def search_for_client():

    last_name = request.form["last_name"]
    owners = owner_repo.select_last_name(last_name)
    return render_template('/view_clients.html',owners=owners)


# function which runs when we click on update button, function actually leads to the update.html page ! 
# DO NOT CHANGE CODE !
@vet_blueprint.route("/search_action/update/<owner_id>", methods=['GET'])
def update_client(owner_id):
    return render_template ("/update.html",owner_id = owner_id)

# function which runs when we submit the updated client
@vet_blueprint.route("/update_action/<owner_id>", methods=['POST'])
def edit_client(owner_id):

    # first get the owner we want to update
    owner = owner_repo.select_by_id(owner_id)
    # second get the animalS we want to update
    animal = animal_repo.select_animal_by_owner(owner)
   
    # at this time FOR TESTING hardcode position [0] only to change the first pets details
    animal[0].name = request.form["name"]
    animal[0].dob = request.form["dob"]
    animal[0].species = request.form["species"]
    animal[0].treatments = request.form["treatments"]
    # here we update the varables in the instance of animal with all the new details from the webForm

    # here we update the instance of the owner's details
    owner.first_name = request.form["first_name"]
    owner.last_name = request.form["last_name"]
    owner.number = request.form ["number"]

    # here we pass the NEW updated Version of the owner instance on to the database
    owner_repo.update(owner)
    # here we pass the New Updated Version of the animal instance to the database
    animal_repo.update(animal[0])

    # this just shows a submit page
    return render_template ('/submit.html')


# function which runs when we click on delete and redirect to Home
# when clicking button it does redirect to Home, but does not yet delete animal
@vet_blueprint.route("/delete/<id>", methods=['GET'])
def delete_owner(id):

    owner = owner_repo.select_by_id(id)
    owner_repo.delete_owner(id)

    return render_template ("/delete.html", owner = owner)





