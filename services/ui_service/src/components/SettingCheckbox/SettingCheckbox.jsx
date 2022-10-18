import { splitProps } from "solid-js";
import styles from './SettingCheckbox.module.css';

function SettingCheckbox(props) {
    const [local, _] = splitProps(props, ['boxid', 'name']);
    return (
        <div class={styles.Checkbox}>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" name={local.boxid} value={local.boxid} id={local.boxid}/>
                <label class="form-check-label" for={local.boxid}>
                    {local.name}
                </label>
            </div>
        </div>
    );
}

export default SettingCheckbox;