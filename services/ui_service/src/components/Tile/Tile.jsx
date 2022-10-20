import styles from './Tile.module.css';
import {children} from "solid-js";

function Tile(props) {
    const c = children(() => props.children);
    return (
        <div class={styles.Tile}> {c()} </div>
    )
}

export default Tile;
