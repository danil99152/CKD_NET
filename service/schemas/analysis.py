from pydantic import BaseModel, conint, confloat


class Analysis(BaseModel):
    priem: conint() = 0
    debjut_v_vozraste: confloat() = 3
    vozrast_gruppa_debjut: conint() = 2
    dz: bool = False
    pol: conint() = 1
    vozrast_gruppy: confloat() = 2
    tr_v_den: conint() = 325
    trpenia_debjut: conint() = 42
    dlit_trpenii: conint() = 20
    nv_v_den: conint() = 133
    er_v_den: confloat() = 4.6
    ley_v_den: confloat() = 11.6
    kr_v_den: conint() = 33
    kr_max: confloat() = 271
    skf_v_den: confloat() = 170
    skf_min: confloat() = 9
    dlit_skf: conint() = 15
    mochevina_v_den: confloat() = 2.3
    mochevina_max: confloat() = 40.1
    alt_v_den: confloat() = 15
    alt_v_max: confloat() = 42.5
    ast_v_den: confloat() = 26
    ast_max: confloat() = 69.9
    ldg_v_den: conint() = 241
    ldg_max: conint() = 1382
    ob_v_den: confloat() = 66
    soe_max: conint() = 20
    soe_v_den: conint() = 8
    srb_max: confloat() = 1.03
    srb_v_den: confloat() = 0.04
    c3_min: confloat() = 1.2
    c4_min: confloat() = 0.28
    gaptoglobin_min: confloat() = 1.22
    cns: bool = False
    porazhenie_cns: bool = False
    porazhenie_serdca: bool = False
    echo_ks: conint() = 0
    chls: conint() = 1
    parenhima_pochek: conint() = 1
    debjut_zabolevaniya: conint() = 2
    gemokolit: bool = False
    diareya: conint() = 2
    temperature: confloat() = 36.6
    rvota: conint() = 2
    ag: bool = 0
    sad: conint() = 90
    dad: conint() = 65
    jkt: conint() = 0
    pechen: conint() = 1
    sut_belok_max: confloat() = 3
    protenuria_dan: conint() = 8
    gematury: conint() = 3
    gematury_dney: conint() = 8
    leykocituria: conint() = 2
    leykuria_dney: conint() = 8
    narushenie_mochespuskania: conint() = 1
    olig_anuria_dney: conint() = 8
    ekulizymab: conint() = 0
    dlit_OPP: conint() = 30
    peritonealny: bool = False
    gemodializ: bool = False
    giuk5: confloat() = 60.574237418639900
    NT5VPlazme: confloat() = 1452.106455894350000




