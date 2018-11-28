export class Friend {
	private id: Number;
	private name: String

	constructor(name: String, id: Number){
		this.name = name;
		this.id = id;
	}

	getId(){
		return this.id;
	}

	setId(id: Number){
		this.id = id;
	}

	getName(){
		return this.name;
	}

	setName(name: String){
		this.name = name;
	}
}