export class Block {
    id: string;
    miner: string;
    difficulty: string;
    timestamp: string;
    
    constructor(id: string, miner: string, difficulty: string, timestamp: string){
        this.id = id;
        this.miner = miner;
        this.difficulty = difficulty;
        this.timestamp = timestamp;
    }
}