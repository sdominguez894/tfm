export class Transaction {
    id    : string;
    from  : string;
    to    : string;
    value : string;
    block : string;

    constructor(id: string, from: string, to: string, value: string, block: string){
        this.id = id;
        this.from = from;
        this.to = to;
        this.value = value;
        this.block = block;
    }
}