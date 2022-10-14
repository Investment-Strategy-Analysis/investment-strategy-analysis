import styles from './Tile.css';
import {children} from "solid-js";

function Tile(props) {
    const c = children(() => props.children);
    return (
        <div class="tile"> {c()} </div>
    )
}

export default Tile;
