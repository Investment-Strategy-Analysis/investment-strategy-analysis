import { splitProps } from "solid-js";

function SettingRadio(props) {
    const [local, _] = splitProps(props, ['name', 'radioid', 'groupname', 'checked']);
    return (
        <>
            <input type="radio" class="btn-check" name={local.groupname} id={local.radioid} autocomplete="off" checked={local.checked}/>
            <label class="btn btn-outline-primary" for={local.radioid}>{local.name}</label>
        </>
    );
}

export default SettingRadio;