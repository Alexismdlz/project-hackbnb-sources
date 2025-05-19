import { NavLink } from "react-router-dom"

/**
 * The header of the application (logo, search bar and top menu)
 */
export const Header = () => {
    return <>
        <div className="max-w-7xl m-auto px-5 py-6 flex justify-between items-center">
            {/* Logo */}
            <div>
                <NavLink to="/">
                    <img src="/img/logo.png" alt="logo" width="160" />
                </NavLink>
            </div>

            {/* Top Menu */}
            <div className="flex items-center gap-4">
                <NavLink to="/booking" className="rounded-4xl border-1 px-[15px] py-[12px] text-gray-300 border-gray-200 flex items-center cursor-pointer">
                    Rechercher une réservation
                </NavLink>
                {/* <HeaderProfile /> */}
            </div>
        </div>
        <hr className="border-gray-200"/>
    </>
}
