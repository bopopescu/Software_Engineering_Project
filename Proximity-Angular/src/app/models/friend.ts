export class Friend {
	private id: Number;
	private lastName: String
	private firstName: String

	constructor(firstName: String, lastName: String, id: Number){
		this.firstName = firstName;
		this.lastName = lastName;
		this.id = id;
	}

	getId(){
		return this.id;
	}

	setId(id: Number){
		this.id = id;
	}

	getName(){
		return this.firstName + " " + this.lastName;
	}

	setName(firstName: String, lastName: String){
		this.firstName = firstName;
		this.lastName = lastName;
	}
}