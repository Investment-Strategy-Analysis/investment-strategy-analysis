import Tile from "../Tile/Tile";

function SettingsTile() {
    return (
        <Tile>
            <div class="block">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault"/>
                    <label class="form-check-label" for="flexCheckDefault">
                        Default checkbox
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked/>
                    <label class="form-check-label" for="flexCheckChecked">
                        Checked checkbox
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked/>
                    <label class="form-check-label" for="flexCheckChecked">
                        Checked checkbox
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked"/>
                    <label class="form-check-label" for="flexCheckChecked">
                        Default checkbox
                    </label>
                </div>
                <hr/>
                <h6>Diversification</h6>
                <div class="btn-group" role="group" aria-label="Diversification">
                    <input type="radio" class="btn-check" name="btnradioDiversification" id="btnradioDiv1" autocomplete="off" checked/>
                    <label class="btn btn-outline-primary" for="btnradioDiv1">High</label>

                    <input type="radio" class="btn-check" name="btnradioDiversification" id="btnradioDiv2" autocomplete="off"/>
                    <label class="btn btn-outline-primary" for="btnradioDiv2">Low</label>
                </div>
                <hr/>
                <h6>Time period:</h6>
                <div class="btn-group" role="group" aria-label="Time period">
                    <input type="radio" class="btn-check" name="btnradioTime" id="btnradioTime1" autocomplete="off" checked/>
                    <label class="btn btn-outline-primary" for="btnradioTime1">1 year</label>

                    <input type="radio" class="btn-check" name="btnradioTime" id="btnradioTime2" autocomplete="off"/>
                    <label class="btn btn-outline-primary" for="btnradioTime2">3 years</label>

                    <input type="radio" class="btn-check" name="btnradioTime" id="btnradioTime3" autocomplete="off"/>
                    <label class="btn btn-outline-primary" for="btnradioTime3">5 years</label>
                </div>
            </div>
        </Tile>
    );
}

export default SettingsTile;
